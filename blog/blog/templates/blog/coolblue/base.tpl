<!DOCTYPE html>
<!--[if IE 7 ]>    <html class="ie7 oldie"> <![endif]-->
<!--[if IE 8 ]>    <html class="ie8 oldie"> <![endif]-->
<!--[if IE 9 ]>    <html class="ie9"> <![endif]-->
<!--[if (gt IE 9)|!(IE)]><!--> <html> <!--<![endif]-->

<head>
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/>
    <meta charset="utf-8"/>
    <meta name="description" content="">
    <meta name="author" content="">
	<meta property="wb:webmaster" content="3caf5a5b94e6991e" />
	
	<link rel="shortcut icon" href="/static/blog/coolblue/images/chine.ico"/>
	
	<title>{% block title %}{% endblock %}残阳似血的博客</title>
	
	{% block css %}
	{% endblock %}
	<link type="text/css" rel="stylesheet" href="/static/blog/coolblue/css/bootstrap.min.css"><link>
	<link rel="stylesheet" type="text/css" media="screen" href="/static/blog/coolblue/css/coolblue.css" />
	<link rel="stylesheet" type="text/css" media="screen" href="/static/blog/coolblue/css/chine.css" />
	
	<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
	<script>window.jQuery || document.write('<script src="/static/blog/coolblue/js/jquery-1.7.2.min.js"><\/script>')</script>
	<script src="/static/blog/coolblue/js/scrollToTop.js"></script>
	<script src="/static/blog/coolblue/js/inputFocusOrBlur.js"></script>
	<script src="/static/blog/coolblue/js/jquery.form.js"></script> 
	<script src="/static/blog/coolblue/js/bootstrap-transition.js"></script> 
	<script src="/static/blog/coolblue/js/bootstrap-tooltip.js"></script>
	<script src="/static/blog/coolblue/js/bootstrap-modal.js"></script> 
	<script src="/static/blog/coolblue/js/subscribe.js"></script> 
	
	<!--[if lt IE 9]>
	    <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->

	{% block js %}
	{% endblock %}
</head>
<body id="top">
	{% block header %}
		{% include "blog/coolblue/nav.html" %}
	{% endblock %}
	
	<!-- content-wrap -->
	<div id="content-wrap">
	
	    <!-- content -->
	    <div id="content" class="clearfix">
	    	
			<!-- main -->
			<div id="main">
				{% block main %}
				{% endblock %}
				
				{% include "blog/coolblue/subscribemodal.html" %}
				{% include "blog/coolblue/modal.html" %}
			<!-- /main -->
			</div>
			{% include "blog/coolblue/sidebar.html" %}
			
	    <!-- content -->
		</div>
	
	<!-- /content-out -->
	</div>
	
	{% block footer %}
		{% include "blog/coolblue/footer.html" %}
	{% endblock %}
	
	{% block footerjs %}
	<script type="text/javascript">
	  window.___gcfg = {lang: 'zh-CN'};
	
	  (function() {
	    var po = document.createElement('script'); po.type = 'text/javascript'; po.async = true;
	    po.src = 'https://apis.google.com/js/plusone.js';
	    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(po, s);
	  })();
	</script>
	{% endblock %}
	
	{% if not settings.debug %}
	<script type="text/javascript">
		var _gaq = _gaq || [];
	    _gaq.push(['_setAccount', 'UA-22437438-1']);
	    _gaq.push(['_trackPageview']);
	
	    (function() {
			var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
	    	ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
	    	var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
		})();
	
	</script>  
	
	{% endif %}
</body>