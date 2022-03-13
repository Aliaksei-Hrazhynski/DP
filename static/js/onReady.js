
// ============= PRELOADER SCRIPT ===================
$(window).load(function() { 
	$('#preloader').addClass('hid');
});
// ============= END PRELOADER SCRIPT ===================
/*closestchild*/
 
        ;(function($){
          $.fn.closestChild = function(selector) {
            var $children, $results;
            
            $children = this.children();
            
            if ($children.length === 0)
              return $();
          
            $results = $children.filter(selector);
            
            if ($results.length > 0)
              return $results;
            else
              return $children.closestChild(selector);
          };
        })(window.jQuery);

/* /. closestchild*/




$(function(){
        var top_show = 280; // В каком положении полосы прокрутки начинать показ кнопки "Наверх"
        var speed = 500; // Скорость прокрутки
    	var $backButton = $('#up'), footerposition;
        
        
    	$(document).scroll(function () { // При прокрутке попадаем в эту функцию
    		/* В зависимости от положения полосы прокрукти и значения top_show, скрываем или открываем кнопку "Наверх" */
       
    		if ($(this).scrollTop() > top_show && $(this).scrollTop() < $(document).height() - $(window).height()-60) {
    			$backButton.fadeIn();
    		}
    		else {
    			$backButton.fadeOut();
    		}
    	});
    	$backButton.click(function () { // При клике по кнопке "Наверх" попадаем в эту функцию
    		/* Плавная прокрутка наверх */
    		scrollto(0, speed);
    	});

        // scrollto
    	window.scrollto = function(destination, speed) {
    		if (typeof speed == 'undefined') {
    			speed = 800;
    		}
    		jQuery("html:not(:animated),body:not(:animated)").animate({scrollTop: destination-60}, speed);
    	};
    	$(".index-template a.scrollto").click(function () {
    		var elementClick = $(this).attr("href")
    		var destination = $(elementClick).offset().top;
    		scrollto(destination);
    		return false;
    	});
    	// end scrollto 

        // fancybox
        $('.fancybox').fancybox({
            padding: 0,
            openEffect  : 'none',
            closeEffect : 'none',
            nextEffect  : 'none',
            prevEffect  : 'none',
            helpers: {
            overlay: {
              locked: false
            }
            }
        });
        
        $('.fancyboxModal').fancybox({
            padding: 0,
            openEffect  : 'none',
            closeEffect : 'none',
            nextEffect  : 'none',
            prevEffect  : 'none',
            fitToView : false, 
            maxWidth: '100%',
            scrolling : "no",
            helpers: {
            overlay: {
              locked: false
            }
            }
        });
        
        // end fancybox
        
        
        
        

        // slick-carousel

            
            $('.top-slider').slick({
                infinite: true,
                slidesToShow: 1,
                slidesToScroll: 1,
                autoplay: true,
                autoplaySpeed: 6000,
                speed: 1500,
                fade: true,
                dots: false,
                prevArrow: '<a href="#" class="slick-prev"><i class="material-icons">navigate_before</i></a>',
                nextArrow: '<a href="#" class="slick-next"><i class="material-icons">navigate_next</i></a>',
                responsive: [
                {
                  breakpoint: 1500,
                  settings: {
                    arrows: false,
                    dots: true
                  }
                }
              ]   
            });
            

        

        
        // validation

    $('.rf').each(function() {
        var item = $(this),
            btn = item.find('.btn');

        function checkInput() {
            item.find('select.required').each(function() {
                if ($(this).val() == '0') {
                    $(this).parents('.form-group').addClass('error');
                    $(this).parents('.form-group').find('.error-message').show();
                } else {
                    $(this).parents('.form-group').removeClass('error');
                }
            });

            item.find('input[type=text].required').each(function() {
                if ($(this).val() != '') {
                    $(this).removeClass('error');
                } else {
                    $(this).addClass('error');
                    $(this).parent('.form-group').find('.error-message').show();
                }
            });

            item.find('textarea.required').each(function() {
                if ($(this).val() != '') {
                    $(this).removeClass('error');
                } else {
                    $(this).addClass('error');
                    $(this).parent('.form-group').find('.error-message').show();
                }
            });

            item.find('input[type=email]').each(function() {
                var regexp = /^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$/i;
                var $this = $(this);
                if ($this.hasClass('required')) {
                    if (regexp.test($this.val())) {
                        $this.removeClass('error');
                    } else {
                        $this.addClass('error');
                        $(this).parent('.form-group').find('.error-message').show();
                    }
                } else {
                    if ($this.val() != '') {
                        if (regexp.test($this.val())) {
                            $this.removeClass('error');
                        } else {

                            $this.addClass('error');
                            $(this).parent('.form-group').find('.error-message').show();
                        }
                    } else {
                        $this.removeClass('error');
                    }
                }
            });


            item.find('input[type=checkbox].required').each(function() {
                if ($(this).is(':checked')) {
                    $(this).removeClass('error');
                } else {
                    $(this).addClass('error');
                    $(this).parent('.form-group').find('.error-message').show();
                }
            });
        }

        btn.click(function() {
            checkInput();
            var sizeEmpty = item.find('.error:visible').length;
            if (sizeEmpty > 0) {
                return false;
            } else {
                item.submit();
                $.fancybox.close();
            }
        });
    });


    $('select').change(function() {
        if ($(this).val() == '') {
            $(this).parents('.form-group').removeClass('selected');
        } else {
            $(this).parents('.form-group').addClass('selected');
            $(this).parents('.form-group').removeClass('error');
        }
    });

    // end validation

        
        
        
    // проверка на Internet Explorer 6-11
    var isIE = /*@cc_on!@*/false || !!document.documentMode;
        
    
    if(isIE){
        $('body').addClass('ie');
    }
    // end
    
    
    
    // lightgallery begin
    
    if($(".lightgallery").length > 0){
        $(".lightgallery").lightGallery({
            selector: 'a.lightgallery-link',
            thumbnail: false
        });
    }
    

    // light gallery end



    
    // retina magic
    
        if (window.devicePixelRatio > 1) {
            var lowresImages = $('img.retina');
        
            lowresImages.each(function(i) {
              var lowres = $(this).attr('src');
              var highres = lowres.replace(".", "_2x.");
              $(this).attr('src', highres);
            });
          }
    
    // end retina

        
        
        
    /* plus minus goods counter */        
        $.fn.globalNumber = function(){
        $('.btn-number').click(function(e){
            e.preventDefault();
            fieldName = $(this).attr('data-field');
            type      = $(this).attr('data-type');
            var input = $("input#"+fieldName);
        
            var currentVal = parseInt(input.val());
            if (!isNaN(currentVal)) {
                if(type == 'minus') {
                    
                    if(currentVal > input.attr('data-min')) {
                        input.val(currentVal - 1).change();
                    } 
                    if(parseInt(input.val()) == input.attr('data-min')) {
                        $(this).attr('disabled', true);
                    }
        
                } else if(type == 'plus') {
        
                    if(currentVal < input.attr('data-max')) {
                        input.val(currentVal + 1).change();
                    }
                    if(parseInt(input.val()) == input.attr('data-max')) {
                        $(this).attr('disabled', true);
                    }
        
                }
            } else {
                input.val(0);
            }
        });
        $('.input-number').focusin(function(){
           $(this).data('oldValue', $(this).val());
        });
        $('.input-number').change(function() {
            
            minValue =  parseInt($(this).attr('data-min'));
            maxValue =  parseInt($(this).attr('data-max'));
            valueCurrent = parseInt($(this).val());
        
            name = $(this).attr('id');
            if(valueCurrent >= minValue) {
                $(".btn-number[data-type='minus'][data-field='"+name+"']").removeAttr('disabled')
            } else {
                alert('К сожалению, было достигнуто минимальное значение');
                $(this).val($(this).data('oldValue'));
            }
            if(valueCurrent <= maxValue) {
                $(".btn-number[data-type='plus'][data-field='"+name+"']").removeAttr('disabled')
            } else {
                alert('К сожалению, было превышено максимальное значение');
                $(this).val($(this).data('oldValue'));
            }
            
            
        });
        $(".input-number").keydown(function (e) {
                // Allow: backspace, delete, tab, escape, enter and .
                if ($.inArray(e.keyCode, [46, 8, 9, 27, 13, 190]) !== -1 ||
                     // Allow: Ctrl+A
                    (e.keyCode == 65 && e.ctrlKey === true) || 
                     // Allow: home, end, left, right
                    (e.keyCode >= 35 && e.keyCode <= 39)) {
                         // let it happen, don't do anything
                         return;
                }
                // Ensure that it is a number and stop the keypress
                if ((e.shiftKey || (e.keyCode < 48 || e.keyCode > 57)) && (e.keyCode < 96 || e.keyCode > 105)) {
                    e.preventDefault();
                }
            });
        };$.fn.globalNumber();
        /* /. plus minus goods counter */  




if ( !$("html").hasClass("touch") ){
            
    if ( !$("body").hasClass("no-animate") ){
        $('.advantages-wrapper .element').addClass("hidden");
        
        
        $('.advantages-wrapper').viewportChecker({
            offset: 600,
            callbackFunction: function(){
                $('.advantages-wrapper .element').addClass("visible animated fadeIn");
                
            }
        });
        
    }
}


        $('.menu-button, .scrollto').click(function(){
            $('.menu-button').toggleClass('active');
            $('.mobile-menu').toggleClass('open');
        });
        $('.mobile-menu, .menu-button').click(function(e){
            if ($(e.target).hasClass('fancyboxModal') == false) {
                e.stopPropagation();
            }
        });
        $('body').click(function(){
            $('.mobile-menu').removeClass('open');
            $('.menu-button').removeClass('active');
        });
        
        
        $('.mobile-menu ul > li').has('ul').addClass('down');
        $('.mobile-menu .down > ul').before('<span class="dropdown-button"></span>');
        

        
        $('.mobile-menu .dropdown-button').click(function(){
            $(this).toggleClass('active');
            if($(this).siblings('ul').is(':visible')){
                $(this).siblings('ul').slideUp();
            }else{
                $(this).siblings('ul').slideDown();
            }
            
        });



});// end ready






jQuery(window).load(function () {
        if ( !$("html").hasClass("touch") ){
            $('.index-text-section').parallax("0", 0.1);
        }
            
}); 














