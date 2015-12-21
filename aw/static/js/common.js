//equal heights
 
(function($) {
	$.fn.equalHeights = function(minHeight, maxHeight) {
		tallest = (minHeight) ? minHeight : 0;
		this.each(function() {
			if($(this).height() > tallest) {
				tallest = $(this).height();
			}
		});
		if((maxHeight) && tallest > maxHeight) tallest = maxHeight;
		return this.each(function() {
			$(this).height(tallest);
		});
	}
})(jQuery);


//http://www.agilecarousel.com/

$(document).ready(function(){


	$('.mainNav li ul').each(function(){
		if ($(this).find('li').length>0){
			$(this).parent('li').addClass('hasSubmenu');
		}

	});
	
	$('.hasSubmenu >a').click(function(e){
		e.preventDefault();
	});
	
  $('.menu-icon').click(function(e){
    e.preventDefault();
    $(this).siblings('.mainNav').slideToggle();
    $(this).siblings('.mainNav').toggleClass('open');
  });	          

  $('.mainNav .hasSubmenu').bind('click', function(){
    if ($(window).width() < 640) {
    $(this).find('ul').slideToggle();
    }
  });

         
	$(".roster-table").tablesorter();
          
	$('.carousel').carousel({
		loop: true,
                autoSlide: false,
                animSpeed: 'slow'  
	});    

       
	if ($('.halfpromo'.length > 0)) {
		    $('.halfpromo.box .whitewrap').equalHeights();
	    }
        
        if ($('.album-list'.length > 0)) {
		    $('.album-list ul li').equalHeights();
	    }        
 	$('.faq li h3 a').click(function(e){
		e.preventDefault();
		$(this).parent('h3').siblings('div.ans').slideToggle(400)
	});       
        
        //http://www.vissit.com/projects/eventCalendar/ 
	
	var url = window.location.href;
	$('.fb-comments').attr('data-href',url);
    
    $('#g1 a').lightBox({
        fixedNavigation:true,
        imageLoading:			'templates/images/lightbox-ico-loading.gif',		// (string) Path and the name of the loading icon
        imageBtnPrev:			'templates/images/lightbox-btn-prev.gif',			// (string) Path and the name of the prev button image
        imageBtnNext:			'templates/images/lightbox-btn-next.gif',			// (string) Path and the name of the next button image
        imageBtnClose:			'templates/images/lightbox-btn-close.gif',		// (string) Path and the name of the close btn
        imageBlank:				'templates/images/lightbox-blank.gif',			// (string) Path and the name of a blank image (one pixel)
     });


		$(".fancybox").fancybox({
		openEffect	: 'none',
		closeEffect	: 'none',
beforeShow: function () {
            if (this.title) {
                // New line
                this.title += '<br />';
           } else {
		this.title = '';
		}
     
                // Add FaceBook like button
                this.title += '<iframe src="//www.facebook.com/plugins/like.php?href=' + this.href + '&amp;layout=button_count&amp;show_faces=true&amp;width=500&amp;action=like&amp;font&amp;colorscheme=light&amp;height=23" scrolling="no" frameborder="0" style="border:none; overflow:hidden; width:110px; height:23px;" allowTransparency="true"></iframe>';
            
        },
        afterShow: function() {
            // Render tweet button
            twttr.widgets.load();
        },
		helpers		: {
			title : {
				type : 'inside'
			},
		}
	});

	if ($('#fb-comment-div').length>0){
		var txt = "<fb:comments href='" + document.location.href + "' num_posts='10' width='620'></fb:comments>";  
		$('#fb-comment-div').html(txt); 
        	FB.XFBML.parse("#fb-comment-div");  
	}

 	setTimeout(function() {
			$('.uiIconText span').css({'color':'#fff'})
		}, 200);
  


});


$(window).resize(function() {
  if ($('.halfpromo'.length > 0)) {
		$('.halfpromo.box .whitewrap').equalHeights();
	}
});




//https://css-tricks.com/NetMag/FluidWidthVideo/Article-FluidWidthVideo.php
$(function() {

    var $allVideos = $("iframe[src^='//player.vimeo.com'], iframe[src^='//www.youtube.com'], object, embed"),
    $fluidEl = $("figure");

  $allVideos.each(function() {

    $(this)
      // jQuery .data does not work on object/embed elements
      .attr('data-aspectRatio', this.height / this.width)
      .removeAttr('height')
      .removeAttr('width');

  });

  $(window).resize(function() {

    var newWidth = $fluidEl.width();
    $allVideos.each(function() {

      var $el = $(this);
      $el
          .width(newWidth)
          .height(newWidth * $el.attr('data-aspectRatio'));

    });

  }).resize();

});
