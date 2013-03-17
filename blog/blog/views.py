#!/usr/bin/env python
#coding=utf-8

from base.util import get_client_ip
from django.conf import settings as settings
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q, Count, Max, Min
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from forms import CommentForm, SubscriberForm
from models import *
from search import GoogleSearch, Record
from utils import process_comment, check_is_robot
import urllib2
import hashlib



blog_theme = getattr(settings, 'BLOG_THEME', 'coolblue')

PAGE_SIZE = 5
PAGE_ENTRY_DISPLAY_NUM = 6
PAGE_ENTRY_EDGE_NUM = 2

MAX_FONT_SIZE = 35
MIN_FONT_SIZE = 12
MINUS_FONT_SIZE = MAX_FONT_SIZE - MIN_FONT_SIZE

admin = settings.ADMINS[0][0]

def common_response(request):
    recent_comments = Comment.visible_objects.order_by('-post_date')
    
    friends = {}
    count = 0
    for comment in recent_comments:
        if count >= 5:
            break
        if comment.username not in friends:
            friends[comment.username] = comment
            count += 1
            
    tags = Tag.objects.annotate(n_articles=Count("articles"))[:25]
    if tags:
        tag_max_articles = tags.aggregate(Max("n_articles"))['n_articles__max']
        tag_min_articles = tags.aggregate(Min("n_articles"))['n_articles__min']
        for tag in tags:
            if tag_max_articles - tag_min_articles > 0:
                tag.font_size = MIN_FONT_SIZE \
                + MINUS_FONT_SIZE*(tag.n_articles-tag_min_articles)/(tag_max_articles-tag_min_articles)
            else:
                tag.font_size = MINUS_FONT_SIZE
                
    try:
        author = BlogUser.objects.get(user__username=admin)
    except BlogUser.DoesNotExist:
        user = User.objects.get(username=admin)
        info = 'Define the user info in the admin interface' # Define the admin info here
        avatar = 'avatar.jpg'
        
        author = BlogUser(small_avatar=avatar, info=info, user=user)
        author.save()
                
    global_settings = {
                'debug': settings.DEBUG,
                'google': settings.ENABLE_GOOGLE_ACCOUNT,
                'weibo': settings.ENABLE_WEIBO_ACCOUNT,
                'renren': settings.ENABLE_RENREN_ACCOUNT,
                'txweibo': settings.ENABLE_QQWEIBO_ACCOUNT
                }
    
    commons = {
            'author': author,
            'categories': Category.objects.all(),
            'populars': Article.objects.order_by('-clicks')[:5],
            'recent_comments': recent_comments[:5],
            'friends': friends.values(),
            'links': Link.objects.all(),
            'tags': tags,
            'settings': global_settings,
            'subscribe_form': SubscriberForm(),
            }
    
    if 'blog_user' in request.session:
        commons['blog_user'] = request.session['blog_user']
    
    return commons
    
def paginator_response(request, page, p):
    # p is an instance of Paginator
    page = int(page)
    size = p.num_pages
    
    left_continual_max = PAGE_ENTRY_EDGE_NUM + PAGE_ENTRY_DISPLAY_NUM / 2 + 1
    left_edge_range = range(1, PAGE_ENTRY_EDGE_NUM + 1)
    left_continual_range = range(1, page)
    left_range = range(page-PAGE_ENTRY_DISPLAY_NUM/2, page+1)
    
    right_continual_min = size - \
        PAGE_ENTRY_DISPLAY_NUM / 2 - 1 \
            if PAGE_ENTRY_DISPLAY_NUM % 2 == 0 \
            else PAGE_ENTRY_DISPLAY_NUM / 2
    right_continual_range = range(page+1, size+1)
    right_edge_range = range(size-PAGE_ENTRY_EDGE_NUM+1, size+1)
    right_range = range(page+1, page+PAGE_ENTRY_EDGE_NUM+1)
    
    vars = locals()
    del vars['size']
    return vars

def handle_session(request, save=False, **kwargs):
    session_data = request.session.get('comment_user', {})
    items = ('username', 'email_address', 'site', 'avatar')
    
    if not save:
        blog_user = request.session.get('blog_user')
        attrs = {
                 'username': 'username', 
                 'email_address': 'email',
                 'site': 'site',
                 'avatar': 'avatar'
                 }
        
        if blog_user:
            # comment_user = {}
            comment_user = session_data
            for k, v in attrs.iteritems():
                if v in blog_user:
                    comment_user[k] = blog_user[v]
            return comment_user
        elif len(session_data) != 0: return session_data
            
    else:
        changed = False
        posts = request.POST
        
        for item in items:
            if session_data.get(item, '') != posts[item]:
                session_data[item] = posts[item]
                if not changed: changed = True
        if kwargs:
            session_data.update(kwargs)
            if not changed: changed = True
                
        if changed: request.session['comment_user'] = session_data

def index(request, page=1):
    p = Paginator(Article.completed_objects.all(), PAGE_SIZE)
    
    try:
        current_page = p.page(page)
    except EmptyPage:
        raise Http404
    articles = current_page.object_list
    
    data = locals()
    data.update(common_response(request))
    data.update(paginator_response(request, page, p))
    
    return render_to_response('blog/%s/index.tpl' % blog_theme, data)

def category(request, slug, page=1):
    category = get_object_or_404(Category, slug=slug)
    
    p = Paginator(Article.completed_objects.filter(category=category), PAGE_SIZE)
    
    try:
        current_page = p.page(page)
    except EmptyPage:
        raise Http404
    articles = current_page.object_list
    
    data = locals()
    data.update(common_response(request))
    if p.num_pages > 1:
        data.update(paginator_response(request, page, p))
    
    return render_to_response('blog/%s/category.tpl' % blog_theme, data)

def tag(request, slug, page=1):
    tag = get_object_or_404(Tag, slug=slug)
    
    p = Paginator(Article.completed_objects.filter(tags__slug=slug), PAGE_SIZE)
    
    try:
        current_page = p.page(page)
    except EmptyPage:
        raise Http404
    articles = current_page.object_list
    
    data = locals()
    data.update(common_response(request))
    if p.num_pages > 1:
        data.update(paginator_response(request, page, p))
    
    return render_to_response('blog/%s/tag.tpl' % blog_theme, data)

def article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    nodes = Comment.to_article_objects.filter(object_id=article.id)
    
    # Comment form
    content_type = ContentType.objects.get(model='article')
    comment_instance = Comment(content_type=content_type, object_id=article.id)
    # Get session data
    session_data = handle_session(request)
    if session_data:
        for item in session_data:
            setattr(comment_instance, item, session_data[item])
    form = CommentForm(instance=comment_instance)
            
    data = {
            'article': article,
            'nodes': nodes,
            'form': form,
            'slug': slug,
            }
    data.update(common_response(request))
    
    if not settings.DEBUG and request.GET.get('from', None) != 'admin':
        article.click_once()
    
    return render_to_response('blog/%s/article.tpl' % blog_theme, data)
    

def categories(request):
    categories_with_articles = Category.objects.all()
    for category in categories_with_articles:
        category.articles = Article.completed_objects.filter(category=category)[:5]
        
    data = locals()
    data.update(common_response(request))
    
    return render_to_response('blog/%s/categories.tpl' % blog_theme, data)

def contact(request):
    user_id = BlogUser.objects.get(user__username=admin).id
    nodes = Comment.to_blog_user_objects.filter(object_id=user_id)
    
    # Comment form
    content_type = ContentType.objects.get(model='bloguser')
    comment_instance = Comment(content_type=content_type, object_id=user_id)
    # Get session data
    session_data = handle_session(request)
    if session_data:
        for item in session_data:
            setattr(comment_instance, item, session_data[item])
    form = CommentForm(instance=comment_instance)
    
    data = {
            'nodes': nodes,
            'form': form
            }
    data.update(common_response(request))
    
    return render_to_response('blog/%s/contact.tpl' % blog_theme, data)

def about(request):
    user = BlogUser.objects.get(user__username=admin)
    
    data = locals()
    data.update(common_response(request))
    
    return render_to_response('blog/%s/about.tpl' % blog_theme, data)

def comment(request):
    response = HttpResponse()
    
    f = CommentForm(request.POST)
    if f.is_valid():
        comment = f.save(commit=False)
        
        comment.content = process_comment(comment.content)
        comment.visible = True
        comment.ip = get_client_ip(request)
        
        if BlackList.objects.filter(ip_address=comment.ip).count() != 0:
            response.write("0")
            return response
        
        if settings.ENABLE_COMMENT_CHN and check_is_robot(comment.content):
            response.write("-1")
            return response
        
        access_gravatar = False
        if not comment.avatar or len(comment.avatar.strip()) == 0:
            email_hash = hashlib.md5(comment.email_address.strip()).hexdigest()
            try:
                avatar_url = 'http://www.gravatar.com/avatar/%s?s=40&d=404' % email_hash
                urllib2.urlopen(avatar_url)
                comment.avatar = avatar_url
                access_gravatar = True
            except urllib2.URLError:
                comment.avatar = ''
        
        comment.save()
        # Handle the session to store the comment info
        if not access_gravatar:
            handle_session(request, True)
        else:
            handle_session(request, True, avatar=comment.avatar)
        
        response.write(str(comment.id))
    else:
        response.write("0")
    
    return response
 
def comments(request, slug):       
    if slug == "bloguser":
        user_id = BlogUser.objects.get(user__username=admin).id
        nodes = Comment.to_blog_user_objects.filter(object_id=user_id)
    else:
        article = get_object_or_404(Article, slug=slug)
        nodes = Comment.to_article_objects.filter(object_id=article.id)
    
    data = locals()
    return render_to_response('blog/%s/comments.tpl' % blog_theme, data)

def search(request, page=1):
    page = int(page)
    
    query = request.GET.get('q', '')
    query = query.strip().replace('Search...', '')
    
    n_per_page = 10
    
    start = (page - 1) * n_per_page + 1
    end = page * n_per_page
    
    count = 0
    if len(query) > 0:
        search = GoogleSearch(query, page)
        count, results = search()
        if count - start + 1 < n_per_page:
            end = count
            
        result_list = [results[i%n_per_page-1] if start <= i <= end else Record() for i in range(1, count+1)]
        p = Paginator(result_list, n_per_page)
        try:
            current_page = p.page(page)
        except EmptyPage:
            raise Http404
        
    data = locals()
    data.update(common_response(request))
    if 'p' in data and p.num_pages > 1:
        data.update(paginator_response(request, page, p))
    
    return render_to_response('blog/%s/search.tpl' % blog_theme, data)

def subscriber(request):
    response = HttpResponse()
    
    f = SubscriberForm(request.POST)
    if f.is_valid():
        subscriber = f.save(commit=False)
        
        sub_objs = Subscriber.objects.filter(email_address=subscriber.email_address)
        if sub_objs.count() == 0:
            subscriber.enabled = True
            subscriber.save()
            
            response.write("1")
        elif sub_objs.count() == 1:
            subscriber = sub_objs[0]
            
            if not subscriber.enabled:
                subscriber.enabled = True
                subscriber.save()
                
                response.write("1")
            else:
                response.write("0")
        else:
            response.write("0")
    else:
        response.write("0")
    
    return response

def unsubscriber(request):
    msg = '取消订阅信息错误'
    
    gets = request.GET
    if 'hv' in gets and 'email' in gets:
        hv = gets['hv']
        email = gets['email']
        
        try:
            subscriber = Subscriber.objects.get(email_address=email)
            
            rht_hv = hashlib.md5(
                        "%s%s"%(subscriber.email_address, str(subscriber.subscribe_time)))\
                        .hexdigest()
            if subscriber.enabled and hv == rht_hv:
                subscriber.enabled = False
                subscriber.save()
                
                msg = '取消订阅成功'
            
        except Subscriber.DoesNotExist:
            pass
        
    data = { 'msg': msg }
    data.update(common_response(request))
    
    return render_to_response('blog/%s/unsubscribe.tpl' % blog_theme, data)