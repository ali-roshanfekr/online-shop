$(document).ready(function () {
    // responsiveMenu
    $('.nav-slider').on('click', function () {
        $('.overlay').show();
        $('nav').toggleClass("open");
    });
    $('.overlay').on('click', function () {
        if ($('nav').hasClass('open')) {
            $('nav').removeClass('open');
        }
        $(this).hide();
    });
    //    header fixed
    $(window).scroll(function () {
        if ($(this).scrollTop() > 0) {
            $('header.header').addClass('fixed');
        } else {
            $('header.header').removeClass('fixed');
        }
    });
    var lastScrollTop = 0;
    window.addEventListener('scroll', function () {
        var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        if (scrollTop > lastScrollTop && !$('.menuMain').hasClass('active')) {
            $('header.header .menuMain').addClass('hidden-menuMain');
            $('header.header .menuMain').slideUp(200);
        } else {
            $('header.header .menuMain').removeClass('hidden-menuMain');
            $('header.header .menuMain').slideDown(200);
        }
        lastScrollTop = scrollTop;
    });
    // niceSelect
    $('select.category').niceSelect();

    // SearchResult
    $('.search-box form input').on('click', function () {
        $(this).parents('.search-box').addClass('show-result').find('.search-result').fadeIn(0);
        $(".overlay-search-box").css({ "opacity": "1", "visibility": "visible" });
    })
    $('.search-box form input').keyup(function () {
        $(this).parents('.search-box').addClass('show-result').find('.search-result').fadeIn(0);
        $(this).parents('.search-box').find('.search-result-list').fadeIn(0);
        if ($(this).val().length == 0) {

            $(this).parents('.search-box').removeClass('show-result').find('.search-result').fadeOut(0);
            $(this).parents('.search-box').find('.search-result-list').fadeOut(0);
            $(this).parents('.search-box').removeClass('show-result');
        } else {

            $(this).parents('.search-box').find('.search-result').fadeIn(0);
            $(this).parents('.search-box').find('.search-result-list').fadeIn(0);
        }
    });
    $(document).click(function (e) {
        if ($(e.target).is('.search-box *')) return;
        $('.search-result').hide();
        $('.search-box').removeClass('show-result');
        $(".overlay-search-box").css({ "opacity": "0", "visibility": "hidden" });
    });

    // offcanvas
    $(document).on('click', '#offcanvas-dismiss-cart, #offcanvas-dismiss-menu, .offcanvas-overlay', function () {
        $('.offcanvas').removeClass('active');
        $('body').removeClass('offcanvas-page');
        $('.offcanvas-overlay').removeClass('active');
    });

    $('#offcanvas-trigger-cart').on('click', function () {
        $('#offcanvasCart').addClass('active');
        $('body').addClass('offcanvas-page');
        $('.offcanvas-overlay').addClass('active');
    });

    // sliderMain
    var swiper = new Swiper(".mainSlider", {
        spaceBetween: 30,
        effect: "fade",
        loop: true,
        centeredSlides: true,
        autoplay: {
            delay: 3000,
            disableOnInteraction: false,
        },
        navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev",
        },
        pagination: {
            el: ".swiper-pagination",
            clickable: true,
        },
        keyboard: true,
    });

    // sliderAmazing
    var swiper = new Swiper(".sliderAmazing", {
        slidesPerView: 5,
        spaceBetween: 3,
        slidesPerGroup: 1,
        loop: true,
        loopFillGroupWithBlank: true,
        breakpoints: {
            300: {
                slidesPerView: 1,
                spaceBetween: 1,
                allowSlidePrev: true,
                allowSlideNext: true,
                mousewheel: true,
                keyboard: true
            },
            470: {
                slidesPerView: 2,
                spaceBetween: 5,
                allowSlidePrev: true,
                allowSlideNext: true,
                mousewheel: true,
                keyboard: true
            },
            640: {
                slidesPerView: 2,
                spaceBetween: 5,
                allowSlidePrev: true,
                allowSlideNext: true,
                mousewheel: true,
                keyboard: true
            },
            768: {
                slidesPerView: 3,
                spaceBetween: 5,
                allowSlidePrev: true,
                allowSlideNext: true,
                mousewheel: true,
                keyboard: true
            },
            1024: {
                slidesPerView: 5,
                spaceBetween: 5,
                allowSlidePrev: true,
                allowSlideNext: true,
                mousewheel: true,
                keyboard: true
            },
            1400: {
                slidesPerView: 5,
                spaceBetween: 5,
                allowSlidePrev: true,
                allowSlideNext: true,
                mousewheel: true,
                keyboard: true
            },
        },
        pagination: {
            el: ".swiper-pagination",
            clickable: true,
        },
        navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev",
        },
    });

    // countdown
    ! function (l) {
        var t = {
            init: function () {
                t.countDown()
            },
            countDown: function (t, i) {
                l(".countdown").each(function () {
                    var t = l(this),
                        a = l(this).data("date-time"),
                        e = l(this).data("labels");
                    (i || t).countdown(a, function (t) {
                        l(this).html(t.strftime('<div class="countdown-item"><div class="countdown-value">%D</div><div class="countdown-label">' + e["label-day"] + '</div></div><div class="countdown-item"><div class="countdown-value">%H</div><div class="countdown-label">' + e["label-hour"] + '</div></div><div class="countdown-item"><div class="countdown-value">%M</div><div class="countdown-label">' + e["label-minute"] + '</div></div><div class="countdown-item"><div class="countdown-value">%S</div><div class="countdown-label">' + e["label-second"] + "</div></div>"))
                    })
                })
            },
        };
        l(function () {
            t.init()
        })
    }(jQuery);

    // sliderProduct
    var swiper = new Swiper(".sliderProduct", {
        slidesPerView: 4,
        spaceBetween: 10,
        slidesPerGroup: 4,
        loopFillGroupWithBlank: true,
        breakpoints: {
            300: {
                slidesPerView: 1,
                spaceBetween: 1,
                allowSlidePrev: true,
                allowSlideNext: true,
                mousewheel: true,
                keyboard: true
            },
            470: {
                slidesPerView: 2,
                spaceBetween: 5,
                allowSlidePrev: true,
                allowSlideNext: true,
                mousewheel: true,
                keyboard: true
            },
            640: {
                slidesPerView: 2,
                spaceBetween: 5,
                allowSlidePrev: true,
                allowSlideNext: true,
                mousewheel: true,
                keyboard: true
            },
            768: {
                slidesPerView: 3,
                spaceBetween: 5,
                allowSlidePrev: true,
                allowSlideNext: true,
                mousewheel: true,
                keyboard: true
            },
            1024: {
                slidesPerView: 5,
                spaceBetween: 5,
                allowSlidePrev: true,
                allowSlideNext: true,
                mousewheel: true,
                keyboard: true
            },
            1400: {
                slidesPerView: 5,
                spaceBetween: 5,
                allowSlidePrev: true,
                allowSlideNext: true,
                mousewheel: true,
                keyboard: true
            },
        },
        pagination: {
            el: ".swiper-pagination",
            clickable: true,
        },
        navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev",
        },
    });
    // cart-item-close
    $('.remove-from-cart-button').on('click', function () {
        Swal.fire({
            text: "آیا مطمئن هستید حذف شود؟",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'بله',
            cancelButtonText: 'خیر'
        }).then((result) => {
            if (result.isConfirmed) {
                Swal.fire({
                    title: 'حذف شد!',
                    confirmButtonText: 'باشه',
                    icon: 'success'
                })
            }
        })
    });
    // add-to-cart
    $('.add-to-cart').on('click', function (event) {
        event.preventDefault();
        const Toast = Swal.mixin({
            toast: true,
            position: 'top-end',
            showConfirmButton: false,
            timer: 3000,
            didOpen: (toast) => {
                toast.addEventListener('mouseenter', Swal.stopTimer)
                toast.addEventListener('mouseleave', Swal.resumeTimer)
            }
        })

        Toast.fire({
            icon: 'success',
            title: 'به سبد خرید خود اضافه شد'
        })
    });
    // compare
    $('.add-to-compare').on('click', function (event) {
        event.preventDefault();
        const Toast = Swal.mixin({
            toast: true,
            position: 'top-end',
            showConfirmButton: false,
            timer: 3000,
            didOpen: (toast) => {
                toast.addEventListener('mouseenter', Swal.stopTimer)
                toast.addEventListener('mouseleave', Swal.resumeTimer)
            }
        })

        Toast.fire({
            icon: 'success',
            title: 'محصول برای مقایسه اضافه شد'
        })
    });
    // wishes 
    $('.add-to-wishlist').on('click', function (event) {
        event.preventDefault();
        const Toast = Swal.mixin({
            toast: true,
            position: 'top-end',
            showConfirmButton: false,
            timer: 3000,
            didOpen: (toast) => {
                toast.addEventListener('mouseenter', Swal.stopTimer)
                toast.addEventListener('mouseleave', Swal.resumeTimer)
            }
        })

        Toast.fire({
            icon: 'success',
            title: 'به لیست علاقه مندی خود اضافه شد'
        })
    });
    // add-to-wishlist
    $(".add-to-wishlist a").on("click", function () {
        $(this).toggleClass("active");
    });
    // sliderMoments
    var swiper = new Swiper(".slider-moments", {
        autoplay: {
            delay: 5000,
            disableOnInteraction: false
        },
        speed: 500,
        loop: true,
        pagination: {
            el: ".swiper-pagination",
            type: "fraction"
        },
        navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev"
        },
        on: {
            init: function () {
                $(".swiper-progress-bar").removeClass("animate");
                $(".swiper-progress-bar").removeClass("active");
                $(".swiper-progress-bar").eq(0).addClass("animate");
                $(".swiper-progress-bar").eq(0).addClass("active");
            },
            slideChangeTransitionStart: function () {
                $(".swiper-progress-bar").removeClass("animate");
                $(".swiper-progress-bar").removeClass("active");
                $(".swiper-progress-bar").eq(0).addClass("active");
            },
            slideChangeTransitionEnd: function () {
                $(".swiper-progress-bar").eq(0).addClass("animate");
            }
        }
    });
    $('.slider-moments').hover(function () {
        swiper.autoplay.stop();
        $('.swiper-progress-bar').removeClass('animate');
    }, function () {
        swiper.autoplay.start();
        $('.swiper-progress-bar').addClass('animate');
    });

    // scrolltop
    $(document).on("scroll", function () {
        var st = $(this).scrollTop();
        if (st > 200) {
            $(".sticky-toolbox").fadeIn(300, "swing");
        } else if (st < 200) {
            $(".sticky-toolbox").fadeOut(300, "swing");
        }
    });
    $(".scroll-sticky").on("click", function () {
        $("html,body").animate({ scrollTop: "0px" }, 1000, "swing");
    });
    $(".gototop").on("click", function () {
        $("html,body").animate({ scrollTop: "0px" }, 1000, "swing");
    });
    // sidebar-sticky
    if ($('.sticky-sidebar').length) {
        $('.sticky-sidebar').theiaStickySidebar();
    }
    //    price-range
    var nonLinearStepSlider = document.getElementById('slider-non-linear-step2');

    if ($('#slider-non-linear-step2').length) {
        noUiSlider.create(nonLinearStepSlider, {
            start: [0, 19000000],
            connect: true,
            direction: 'rtl',
            format: wNumb({
                decimals: 0,
                thousand: ','
            }),
            range: {
                'min': [0],
                '10%': [500, 500],
                '50%': [40000, 1000],
                'max': [19000000]
            }
        });
        var nonLinearStepSliderValueElement = document.getElementById('slider-non-linear-step-value2');

        nonLinearStepSlider.noUiSlider.on('update', function (values) {
            nonLinearStepSliderValueElement.innerHTML = values.join(' - ');
        });
    }
    // sidebar
    $(document).on('click', '#sidebar-dismiss-cart, .sidebar-overlay', function () {
        $('.togglesidebar').removeClass('active');
        $('body').removeClass('sidebar-page');
        $('.sidebar-overlay').removeClass('active');
    });

    $('#sidebar-trigger-cart').on('click', function () {
        $('.togglesidebar').addClass('active');
        $('body').addClass('sidebar-page');
        $('.sidebar-overlay').addClass('active');
    });
    // tab
    $(".mask-handler").click(function (e) {
        e.preventDefault();
        var sumaryBox = $(this).parents('.content-expert-summary');
        sumaryBox.find('.mask-text').toggleClass('active');
        sumaryBox.find('.shadow-box').fadeToggle(0);
        $(this).find('.show-more').fadeToggle(0);
        $(this).find('.show-less').fadeToggle(0);
    });
    //    quantity-selector
    jQuery('<div class="quantity-nav"><div class="quantity-button quantity-up">+</div><div class="quantity-button quantity-down">-</div></div>').insertAfter('.quantity input');
    jQuery('.quantity').each(function () {
        var spinner = jQuery(this),
            input = spinner.find('input[type="number"]'),
            btnUp = spinner.find('.quantity-up'),
            btnDown = spinner.find('.quantity-down'),
            min = input.attr('min'),
            max = input.attr('max');

        btnUp.click(function () {
            var oldValue = parseFloat(input.val());
            if (oldValue >= max) {
                var newVal = oldValue;
            } else {
                var newVal = oldValue + 1;
            }
            spinner.find("input").val(newVal);
            spinner.find("input").trigger("change");
        });

        btnDown.click(function () {
            var oldValue = parseFloat(input.val());
            if (oldValue <= min) {
                var newVal = oldValue;
            } else {
                var newVal = oldValue - 1;
            }
            spinner.find("input").val(newVal);
            spinner.find("input").trigger("change");
        });

    });
    // showcoupon
    $("a.showcoupon").click(function () {
        $(".checkout-coupon").slideToggle(200);
    });
    // shipping_address
    $(".woocommerce-shipping-fields .form-auth-row").click(function () {
        $(".shipping-address").slideToggle(200);
    });
    // notify
    $(".meta-notify .more").click(function () {
        $(".widget-content .content").slideToggle(200);
    });
    //    verify-phone-number
    if ($("#countdown-verify-end").length) {
        var $countdownOptionEnd = $("#countdown-verify-end");

        $countdownOptionEnd.countdown({
            date: (new Date()).getTime() + 180 * 1000, // 1 minute later
            text: '<span class="day">%s</span><span class="hour">%s</span><span>: %s</span><span>%s</span>',
            end: function () {
                $countdownOptionEnd.html("<a href='' class='link-border-verify form-account-link'>ارسال مجدد</a>");
            }
        });
    }
    $(".line-number-account").keyup(function () {
        $(this).next().focus();
    });
    // galleryProduct
    $('img.light-zoom').lightzoom({
        zoomPower: 3,    //Default
        glassSize: 200,  //Default
    });

    if ($('.gallery-slider').length) {
        var gallerySlider = new Swiper('.gallery-slider', {
            centeredSlides: true,
            pagination: {
                el: '.swiper-pagination',
                clickable: true,
                dynamicBullets: true,
            },
        });
        var gallerySliderThumbs = new Swiper('.gallery-slider-thumbs', {
            slidesPerView: 5,
            touchRatio: 0.2,
            slideToClickedSlide: true,
            centeredSlides: true,
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            },
        });
        gallerySlider.controller.control = gallerySliderThumbs;
        gallerySliderThumbs.controller.control = gallerySlider;
    }
    $('.products-gallery').magnificPopup({
        delegate: 'a.image-popup-vertical-fit',
        type: 'image',
        mainClass: 'mfp-img-mobile',
        gallery: {
            enabled: true,
            navigateByImgClick: true,
            preload: [0, 1] // Will preload 0 - before current, and 1 after the current image
        }
    });
    // advantages
    var inputs = $('#advantage-input, #disadvantage-input');
    var inputChangeCallback = function () {
        var self = $(this);
        if (self.val().trim().length > 0) {
            self.siblings('.js-icon-form-add').show();
        } else {
            self.siblings('.js-icon-form-add').hide();
        }
    };
    inputs.each(function () {
        inputChangeCallback.bind(this)();
        $(this).on('change keyup', inputChangeCallback.bind(this));
    });
    $("#advantages").delegate(".js-icon-form-add", 'click', function (e) {

        var parent = $('.js-advantages-list');
        if (parent.find(".js-advantage-item").length >= 5) {
            return;
        }

        var advantageInput = $('#advantage-input');

        if (advantageInput.val().trim().length > 0) {
            parent.append(
                '<div class="ui-dynamic-label ui-dynamic-label--positive js-advantage-item">\n' +
                advantageInput.val() +
                '<button type="button" class="ui-dynamic-label-remove js-icon-form-remove"></button>\n' +
                '<input type="hidden" name="comment[advantages][]" value="' + advantageInput
                    .val() + '">\n' +
                '</div>');

            advantageInput.val('').change();
            advantageInput.focus();
        }

    }).delegate(".js-icon-form-remove", 'click', function (e) {
        $(this).parent('.js-advantage-item').remove();
    });

    $("#disadvantages").delegate(".js-icon-form-add", 'click', function (e) {

        var parent = $('.js-disadvantages-list');
        if (parent.find(".js-disadvantage-item").length >= 5) {
            return;
        }

        var disadvantageInput = $('#disadvantage-input');

        if (disadvantageInput.val().trim().length > 0) {
            parent.append(
                '<div class="ui-dynamic-label ui-dynamic-label--negative js-disadvantage-item">\n' +
                disadvantageInput.val() +
                '<button type="button" class="ui-dynamic-label-remove js-icon-form-remove"></button>\n' +
                '<input type="hidden" name="comment[disadvantages][]" value="' +
                disadvantageInput.val() + '">\n' +
                '</div>');

            disadvantageInput.val('').change();
            disadvantageInput.focus();
        }

    }).delegate(".js-icon-form-remove", 'click', function (e) {
        $(this).parent('.js-disadvantage-item').remove();
    });
});