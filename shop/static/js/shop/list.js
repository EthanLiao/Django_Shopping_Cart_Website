var slideIndex = 0;
var slideTimeout;
var intervalTime=5000;

showSlidesAuto();

function plusSlides(n){
  clearTimeout(slideTimeout);
  showSlidesStatic(slideIndex+=n);
  slideTimeout = setTimeout(showSlidesAuto, intervalTime);
}

function currentSlide(n) {
  clearTimeout(slideTimeout); // when trigger in a new graph, we can clear the time out
                              // then start below
  showSlidesStatic(slideIndex = n);
  slideTimeout = setTimeout(showSlidesAuto, intervalTime);
}


function showSlidesStatic(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
  //sleep(2000);
}

function showSlidesAuto() {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  // dot 會變黑
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
  slideTimeout = setTimeout(showSlidesAuto, intervalTime); // Change image every 2 seconds
}

/*Below two functions are for onmouseover outmouseover event handler*/
function pauseSlideshow(){
  clearTimeout(slideTimeout);
}

function startSlideshow(){
  slideTimeout = setTimeout(showSlidesAuto, intervalTime);
}
