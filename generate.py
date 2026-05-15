D=chr(36)
A=chr(38)
html=f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Brew {A}amp; Bean - Specialty Coffee House</title>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700{A}family=Raleway:wght@300;400;600{A}display=swap" rel="stylesheet">
    <link rel="stylesheet" href="fontawesome/css/all.min.css">
    <link rel="stylesheet" href="css/brew-bean.css">
</head>
<body>
  <div class="bb-container">
    <div class="bb-row">
      <div class="bb-left">
        <div class="bb-left-inner">
          <div class="bb-site-header">
            <i class="fas fa-mug-hot fa-3x bb-site-logo"></i>
            <h1 class="bb-site-name">Brew {A}amp; Bean</h1>
            <p class="bb-tagline">Crafted with Passion</p>
          </div>
          <nav class="bb-site-nav">
            <ul class="bb-site-nav-ul">
              <li class="bb-page-nav-item">
                <a href="#menu" class="bb-page-link active">
                  <i class="fas fa-coffee bb-page-link-icon"></i>
                  <span>Menu</span>
                </a>
              </li>
              <li class="bb-page-nav-item">
                <a href="#about" class="bb-page-link ">
                  <i class="fas fa-leaf bb-page-link-icon"></i>
                  <span>Our Story</span>
                </a>
              </li>
              <li class="bb-page-nav-item">
                <a href="#special" class="bb-page-link ">
                  <i class="fas fa-star bb-page-link-icon"></i>
                  <span>Specials</span>
                </a>
              </li>
              <li class="bb-page-nav-item">
                <a href="#contact" class="bb-page-link ">
                  <i class="fas fa-envelope bb-page-link-icon"></i>
                  <span>Contact</span>
                </a>
              </li>
            </ul>
          </nav>
          <div class="bb-sidebar-footer">
            <p class="bb-hours-title">Open Hours</p>
            <p class="bb-hours">Mon-Fri: 7AM - 8PM<br>Sat-Sun: 8AM - 10PM</p>
            <div class="bb-social">
              <a href="#" class="bb-social-link"><i class="fab fa-facebook-f"></i></a>
              <a href="#" class="bb-social-link"><i class="fab fa-instagram"></i></a>
              <a href="#" class="bb-social-link"><i class="fab fa-twitter"></i></a>
            </div>
          </div>
        </div>
      </div>
      <div class="bb-right">
        <main class="bb-main">
          <div id="menu" class="bb-page-content">
            <nav class="bb-black-bg bb-menu-nav">
              <ul>
                <li><a href="#" class="bb-tab-link active" data-id="cold">Iced Coffee</a></li>
                <li><a href="#" class="bb-tab-link" data-id="hot">Hot Coffee</a></li>
                <li><a href="#" class="bb-tab-link" data-id="juice">Smoothies</a></li>
                <li><a href="#" class="bb-tab-link" data-id="pastry">Pastries</a></li>
              </ul>
            </nav>
            <div id="cold" class="bb-tab-content"><div class="bb-list">
            <div id="hot" class="bb-tab-content"><div class="bb-list">
            <div id="juice" class="bb-tab-content"><div class="bb-list">
            <div id="pastry" class="bb-tab-content"><div class="bb-list">
                <div class="bb-list-item">
                  <img src="img/iced-americano.png" alt="Iced Americano" class="bb-list-item-img">
                  <div class="bb-black-bg bb-list-item-text">
                    <h3 class="bb-list-item-name">Iced Americano<span class="bb-list-item-price">{D}4.50</span></h3>
                    <p class="bb-list-item-description">Double shot espresso poured over ice with a splash of cold water. Refreshing and bold.</p>
                  </div>
                </div>
                <div class="bb-list-item">
                  <img src="img/iced-cappuccino.png" alt="Iced Cappuccino" class="bb-list-item-img">
                  <div class="bb-black-bg bb-list-item-text">
                    <h3 class="bb-list-item-name">Iced Cappuccino<span class="bb-list-item-price">{D}5.25</span></h3>
                    <p class="bb-list-item-description">Espresso with cold milk poured over ice, topped with a thick layer of frothed milk.</p>
                  </div>
                </div>
                <div class="bb-list-item">
                  <img src="img/iced-espresso.png" alt="Iced Espresso" class="bb-list-item-img">
                  <div class="bb-black-bg bb-list-item-text">
                    <h3 class="bb-list-item-name">Iced Espresso<span class="bb-list-item-price">{D}3.75</span></h3>
                    <p class="bb-list-item-description">A double shot of our signature espresso blend served over ice. Pure coffee intensity.</p>
                  </div>
                </div>
                <div class="bb-list-item">
                  <img src="img/iced-latte.png" alt="Iced Latte" class="bb-list-item-img">
                  <div class="bb-black-bg bb-list-item-text">
                    <h3 class="bb-list-item-name">Iced Latte<span class="bb-list-item-price">{D}5.50</span></h3>
                    <p class="bb-list-item-description">Espresso combined with chilled milk and ice. Silky smooth and perfectly balanced.</p>
                  </div>
                </div>
              </div></div>
                <div class="bb-list-item">
                  <img src="img/hot-americano.png" alt="Hot Americano" class="bb-list-item-img">
                  <div class="bb-black-bg bb-list-item-text">
                    <h3 class="bb-list-item-name">Hot Americano<span class="bb-list-item-price">{D}3.50</span></h3>
                    <p class="bb-list-item-description">Espresso shots topped with hot water to create a light layer of crema. Simple and classic.</p>
                  </div>
                </div>
                <div class="bb-list-item">
                  <img src="img/hot-cappuccino.png" alt="Hot Cappuccino" class="bb-list-item-img">
                  <div class="bb-black-bg bb-list-item-text">
                    <h3 class="bb-list-item-name">Hot Cappuccino<span class="bb-list-item-price">{D}4.75</span></h3>
                    <p class="bb-list-item-description">Rich espresso with steamed milk, topped with a thick layer of foam and a dusting of cocoa.</p>
                  </div>
                </div>
                <div class="bb-list-item">
                  <img src="img/hot-espresso.png" alt="Hot Espresso" class="bb-list-item-img">
                  <div class="bb-black-bg bb-list-item-text">
                    <h3 class="bb-list-item-name">Hot Espresso<span class="bb-list-item-price">{D}3.00</span></h3>
                    <p class="bb-list-item-description">Our signature single-origin espresso, pulled to perfection with a rich crema layer.</p>
                  </div>
                </div>
                <div class="bb-list-item">
                  <img src="img/hot-latte.png" alt="Hot Latte" class="bb-list-item-img">
                  <div class="bb-black-bg bb-list-item-text">
                    <h3 class="bb-list-item-name">Hot Latte<span class="bb-list-item-price">{D}4.50</span></h3>
                    <p class="bb-list-item-description">Espresso with steamed milk and a light layer of foam. Our most popular hot beverage.</p>
                  </div>
                </div>
              </div></div>
                <div class="bb-list-item">
                  <img src="img/smoothie-1.png" alt="Strawberry Smoothie" class="bb-list-item-img">
                  <div class="bb-black-bg bb-list-item-text">
                    <h3 class="bb-list-item-name">Strawberry Bliss<span class="bb-list-item-price">{D}6.50</span></h3>
                    <p class="bb-list-item-description">Fresh strawberries blended with yogurt and honey. A refreshing burst of summer flavor.</p>
                  </div>
                </div>
                <div class="bb-list-item">
                  <img src="img/smoothie-2.png" alt="Berry Smoothie" class="bb-list-item-img">
                  <div class="bb-black-bg bb-list-item-text">
                    <h3 class="bb-list-item-name">Berry Burst<span class="bb-list-item-price">{D}6.75</span></h3>
                    <p class="bb-list-item-description">Mixed berries, banana, and a splash of almond milk. Packed with antioxidants.</p>
                  </div>
                </div>
                <div class="bb-list-item">
                  <img src="img/smoothie-3.png" alt="Pineapple Smoothie" class="bb-list-item-img">
                  <div class="bb-black-bg bb-list-item-text">
                    <h3 class="bb-list-item-name">Tropical Twist<span class="bb-list-item-price">{D}7.00</span></h3>
                    <p class="bb-list-item-description">Pineapple, mango, coconut milk, and a hint of lime. Your tropical escape in a cup.</p>
                  </div>
                </div>
                <div class="bb-list-item">
                  <img src="img/smoothie-4.png" alt="Green Smoothie" class="bb-list-item-img">
                  <div class="bb-black-bg bb-list-item-text">
                    <h3 class="bb-list-item-name">Green Goddess<span class="bb-list-item-price">{D}7.25</span></h3>
                    <p class="bb-list-item-description">Spinach, kale, apple, ginger, and lemon. A nutritious powerhouse to start your day.</p>
                  </div>
                </div>
              </div></div>
                <div class="bb-list-item">
                  <img src="img/special-01.jpg" alt="Croissant" class="bb-list-item-img">
                  <div class="bb-black-bg bb-list-item-text">
                    <h3 class="bb-list-item-name">Butter Croissant<span class="bb-list-item-price">{D}3.50</span></h3>
                    <p class="bb-list-item-description">Flaky, golden-brown French croissant made with layers of butter. Baked fresh daily.</p>
                  </div>
                </div>
                <div class="bb-list-item">
                  <img src="img/special-02.jpg" alt="Blueberry Muffin" class="bb-list-item-img">
                  <div class="bb-black-bg bb-list-item-text">
                    <h3 class="bb-list-item-name">Blueberry Muffin<span class="bb-list-item-price">{D}3.75</span></h3>
                    <p class="bb-list-item-description">Moist muffin loaded with wild blueberries and topped with a crumbly streusel.</p>
                  </div>
                </div>
                <div class="bb-list-item">
                  <img src="img/special-03.jpg" alt="Chocolate Cake" class="bb-list-item-img">
                  <div class="bb-black-bg bb-list-item-text">
                    <h3 class="bb-list-item-name">Chocolate Fudge Cake<span class="bb-list-item-price">{D}5.50</span></h3>
                    <p class="bb-list-item-description">Rich, decadent chocolate layer cake with a silky ganache frosting. A chocoholic dream.</p>
                  </div>
                </div>
                <div class="bb-list-item">
                  <img src="img/special-04.jpg" alt="Cinnamon Roll" class="bb-list-item-img">
                  <div class="bb-black-bg bb-list-item-text">
                    <h3 class="bb-list-item-name">Cinnamon Roll<span class="bb-list-item-price">{D}4.25</span></h3>
                    <p class="bb-list-item-description">Soft, pillowy dough swirled with cinnamon sugar and topped with cream cheese icing.</p>
                  </div>
                </div>
              </div></div>
          </div>
          <div id="about" class="bb-page-content">
            <div class="bb-black-bg bb-mb-20 bb-about-box-1">
              <h2 class="bb-text-primary bb-about-header">Our Story</h2>
              <div class="bb-list-item bb-list-item-2">
                <img src="img/about-1.png" alt="Our coffee shop" class="bb-list-item-img bb-list-item-img-big">
                <div class="bb-list-item-text-2">
                  <p>Brew {A}amp; Bean was born from a simple belief: that great coffee has the power to bring people together. Founded in 2015, we source the finest beans from sustainable farms around the world.</p>
                  <p>Every cup we serve is roasted in-house and crafted with care. We are not just a coffee shop - we are a community space where stories are shared and connections are made.</p>
                </div>
              </div>
            </div>
            <div class="bb-black-bg bb-mb-20 bb-about-box-2">
              <div class="bb-list-item bb-list-item-2">
                <div class="bb-list-item-text-2">
                  <h2 class="bb-text-primary">Our Values</h2>
                  <p><strong>Sustainability:</strong> We partner with farms that practice ethical farming and fair trade.</p>
                  <p><strong>Quality:</strong> From bean to cup, we never compromise on quality.</p>
                  <p><strong>Community:</strong> We host local artists, musicians, and events to support our neighborhood.</p>
                </div>
                <img src="img/about-2.png" alt="Our values" class="bb-list-item-img bb-list-item-img-big bb-img-right">
              </div>
            </div>
          </div>
          <div id="special" class="bb-page-content">
            <h2 class="bb-section-title bb-black-bg">Chef Specials</h2>
            <div class="bb-special-items">
              <div class="bb-black-bg bb-special-item">
                <img src="img/special-01.jpg" alt="Hazelnut Latte">
                <div class="bb-special-item-description">
                  <h3 class="bb-text-primary bb-special-item-title">Hazelnut Dream Latte</h3>
                  <p class="bb-special-item-text">Our signature latte with house-made hazelnut syrup, topped with whipped cream and caramel drizzle.</p>
                  <span class="bb-special-item-price">{D}6.50</span>
                </div>
              </div>
              <div class="bb-black-bg bb-special-item">
                <img src="img/special-02.jpg" alt="Matcha Latte">
                <div class="bb-special-item-description">
                  <h3 class="bb-text-primary bb-special-item-title">Ceremonial Matcha</h3>
                  <p class="bb-special-item-text">Premium Japanese matcha whisked with steamed oat milk. Earthy, creamy, and vibrant green.</p>
                  <span class="bb-special-item-price">{D}5.75</span>
                </div>
              </div>
              <div class="bb-black-bg bb-special-item">
                <img src="img/special-03.jpg" alt="Cold Brew">
                <div class="bb-special-item-description">
                  <h3 class="bb-text-primary bb-special-item-title">Nitro Cold Brew</h3>
                  <p class="bb-special-item-text">Slow-steeped for 24 hours, infused with nitrogen for a silky-smooth, creamy finish. No ice needed.</p>
                  <span class="bb-special-item-price">{D}5.00</span>
                </div>
              </div>
              <div class="bb-black-bg bb-special-item">
                <img src="img/special-04.jpg" alt="Chai Latte">
                <div class="bb-special-item-description">
                  <h3 class="bb-text-primary bb-special-item-title">Spiced Chai Latte</h3>
                  <p class="bb-special-item-text">House-blend chai spices simmered with honey and steamed milk. Warmth in every sip.</p>
                  <span class="bb-special-item-price">{D}5.25</span>
                </div>
              </div>
              <div class="bb-black-bg bb-special-item">
                <img src="img/special-05.jpg" alt="Affogato">
                <div class="bb-special-item-description">
                  <h3 class="bb-text-primary bb-special-item-title">Affogato Delight</h3>
                  <p class="bb-special-item-text">A scoop of vanilla gelato topped with a hot shot of espresso. The perfect sweet-caffeine treat.</p>
                  <span class="bb-special-item-price">{D}6.00</span>
                </div>
              </div>
              <div class="bb-black-bg bb-special-item">
                <img src="img/special-06.jpg" alt="Mocha">
                <div class="bb-special-item-description">
                  <h3 class="bb-text-primary bb-special-item-title">Dark Mocha</h3>
                  <p class="bb-special-item-text">Rich dark chocolate ganache blended with our double espresso and steamed oat milk. Decadent and bold.</p>
                  <span class="bb-special-item-price">{D}5.75</span>
                </div>
              </div>
            </div>
          </div>
          <div id="contact" class="bb-page-content">
            <div class="bb-black-bg bb-contact-text-container">
              <h2 class="bb-text-primary">Get in Touch</h2>
              <p>Have a question, feedback, or want to book our space for an event? We would love to hear from you! Drop us a message and we will get back to you within 24 hours.</p>
              <div class="bb-contact-info">
                <p><i class="fas fa-map-marker-alt"></i> 123 Bean Street, Coffeeville, WA 98001</p>
                <p><i class="fas fa-phone"></i> (555) 123-4567</p>
                <p><i class="fas fa-envelope"></i> hello@brewnbean.com</p>
              </div>
            </div>
            <div class="bb-black-bg bb-contact-form-container bb-align-right">
              <form action="" method="POST" id="contact-form">
                <div class="bb-form-group">
                  <input type="text" name="name" class="bb-form-control" placeholder="Your Name" required />
                </div>
                <div class="bb-form-group">
                  <input type="email" name="email" class="bb-form-control" placeholder="Your Email" required />
                </div>
                <div class="bb-form-group">
                  <input type="text" name="subject" class="bb-form-control" placeholder="Subject" />
                </div>
                <div class="bb-form-group bb-mb-30">
                  <textarea rows="5" name="message" class="bb-form-control" placeholder="Your Message" required></textarea>
                </div>
                <div>
                  <button type="submit" class="bb-btn-primary bb-align-right">
                    Send Message <i class="fas fa-paper-plane"></i>
                  </button>
                </div>
              </form>
            </div>
          </div>
        </main>
        <footer class="bb-site-footer">
          <p class="bb-black-bg bb-footer-text">{A}copy; 2024 Brew {A}amp; Bean Coffee House. All rights reserved.</p>
        </footer>
      </div>
    </div>
  </div>
  <div class="bb-video-wrapper">
      <i id="bb-video-control-button" class="fas fa-pause"></i>
      <video autoplay muted loop id="bb-video">
          <source src="video/wave-cafe-video-bg.mp4" type="video/mp4">
      </video>
  </div>
  <script src="js/jquery-3.4.1.min.js"></script>
  <script>
    function setVideoSize(){{
      var vidWidth=1920;var vidHeight=1080;
      var ww=window.innerWidth;var wh=window.innerHeight;
      var tempVidWidth=wh*vidWidth/vidHeight;
      var tempVidHeight=ww*vidHeight/vidWidth;
      var nw=tempVidWidth>ww?tempVidWidth:ww;
      var nh=tempVidHeight>wh?tempVidHeight:wh;
      var v=jQuery;v("#bb-video").css("width",nw).css("height",nh);
    }}
    function openTab(e,i){{
      jQuery(".bb-tab-content").hide();
      jQuery("#"+i).show();
      jQuery(".bb-tab-link").removeClass("active");
      jQuery(e.currentTarget).addClass("active");
    }}
    function initPage(){{
      var p=location.hash;
      if(p){{highlightMenu(jQuery(".bb-page-link[href^=""{D}{{p}}""]"));showPage(jQuery(p));}}
      else{{p=jQuery(".bb-page-link.active").attr("href");showPage(jQuery(p));}}
    }}
    function highlightMenu(m){{
      jQuery(".bb-page-link").removeClass("active");m.addClass("active");
    }}
    function showPage(p){{
      jQuery(".bb-page-content").hide();p.show();
    }}
    jQuery(document).ready(function(){{
      initPage();
      jQuery(".bb-page-link").click(function(e){{
        if(window.innerWidth>991){{e.preventDefault();}}
        highlightMenu(jQuery(e.currentTarget));showPage(jQuery(e.currentTarget.hash));
      }});
      jQuery(".bb-tab-link").on("click",function(e){{
        e.preventDefault();openTab(e,jQuery(e.target).data("id"));
      }});
      jQuery(".bb-tab-link.active").click();
      setVideoSize();
      var t;window.onresize=function(){{clearTimeout(t);t=setTimeout(setVideoSize,100);}};
      var b=jQuery("#bb-video-control-button");
      b.on("click",function(e){{
        var v=document.getElementById("bb-video");jQuery(this).removeClass();
        if(v.paused){{v.play();jQuery(this).addClass("fas fa-pause");}}
        else{{v.pause();jQuery(this).addClass("fas fa-play");}}
      }});
      jQuery("#contact-form").on("submit",function(e){{
        e.preventDefault();alert("Thank you for reaching out! We will get back to you soon.");this.reset();
      }});
    }});
  </script>
</body>
</html>
"""

with open("index.html","w",encoding="utf-8") as f:
    f.write(html)
print("index.html created - "+str(len(html))+" bytes")