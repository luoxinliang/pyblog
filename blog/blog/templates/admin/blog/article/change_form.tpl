{% extends "admin/change_form.html" %}

{% block javascripts %}
    {{ block.super }}
	<script type="text/javascript" charset="utf-8">
		var newWin;
		var newWinOpen = false;
		
		(function($) {
			$(function() {
				$.get('/admin/check_weibo_auth/', function(data) {
					if(data == "0") {
						$("div.share div.span-flexible").append(
							"<a id='admin_weibo_auth' href='/admin/weibo/auth/' title='新浪微博未授权或已过期，点击授权' onclick='return openNewWindow(this);'>"
							+ "<img src='/static/blog/coolblue/images/weibo_16.png' style='margin:0 0 0 10px;'></a>");
						var checkNewWinClosed = setInterval(function() {
							if(newWinOpen && newWin.closed) {
								$('a#admin_weibo_auth').remove();
								window.clearInterval(checkNewWinClosed);
							}
						}, 500);
					}
				});
			});
		})(django.jQuery);
		
		function openNewWindow(triggerLink) {
			newWin = window.open(triggerLink.href, "weibo_auth", 'height=500,width=980,resizable=yes,scrollbars=yes')
			newWin.focus();
			if(!newWinOpen) newWinOpen = true;
			return false;
		}
	</script>
{% endblock %}