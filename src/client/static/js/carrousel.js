const SLIDE_TIMEOUT = 5000;
const PREV_SLIDE = document.getElementById('prev');
const NEXT_SLIDE = document.getElementById('next');
const $SLIDES = Array.from(document.querySelectorAll('.project'));
const TOTAL_SLIDES = $SLIDES.length;
const FIRST_SLIDE = 0;
let $dots;
let intervalId;
let currentSlide = 0;

/**
 * Initialize dots.
 * Create dots for each slide and add event listeners for navigation.
 */
function initDots() {
    for (let i = 1; i <= TOTAL_SLIDES; i++) {
        let dotClass = i === currentSlide + 1 ? 'active' : 'inactive';
        let $dot = `<span data-slideId="${i}" class="dot ${dotClass}"></span>`;
        document.querySelector('.carousel-dots').innerHTML += $dot;
    }
    $dots = document.querySelectorAll('.dot');
    // Add click event listeners to each dot
    $dots.forEach(($elt, key) => $elt.addEventListener('click', () => slideTo(key)));
}

/**
 * Initialize buttons.
 * Add event listeners for previous and next buttons.
 */
function initButtons() {
    PREV_SLIDE.addEventListener('click', () => {
        slideTo(--currentSlide);
    });
    NEXT_SLIDE.addEventListener('click', () => {
        slideTo(++currentSlide);
    });
}

/**
 * Initialize intervals variable and add event listeners for mouse and touch events.
 */
function initIntervals() {
    intervalId = setInterval(showNextSlide, SLIDE_TIMEOUT);
    $SLIDES.forEach(($slide) => {
        let startX;
        let endX;
        // Clear slide display interval when mouse hovers over a slide
        $slide.addEventListener('mouseover', () => {
            clearInterval(intervalId);
        }, false)

        // Reset slide display interval when mouse leaves a slide
        $slide.addEventListener('mouseout', () => {
            intervalId = setInterval(showSlide, SLIDE_TIMEOUT);
        }, false);

        // Record initial touch position when user touches a slide
        $slide.addEventListener('touchstart', (event) => {
            startX = event.touches[0].clientX;
        });

        // Record final touch position when user releases finger
        $slide.addEventListener('touchend', (event) => {
            endX = event.changedTouches[0].clientX;
            if (startX > endX) {
                slideTo(currentSlide + 1);
            } else if (startX < endX) {
                slideTo(currentSlide - 1);
            }
        });
    });
}

/**
 * Show specific slide with index.
 * @param {number} index - Index of the slide to show.
 */
function slideTo(index) {
    console.log(index);
    if (index >= TOTAL_SLIDES) 
        currentSlide = FIRST_SLIDE;
    else if(index < FIRST_SLIDE)
        currentSlide = TOTAL_SLIDES - 1;
    else 
        currentSlide = index;


    $SLIDES.forEach(($slide) => {
        $slide.style.transform = `translateX(-${currentSlide * 100}%)`;
    });

    // Update dot colors based on current slide
    $dots.forEach(($slide, key) => {
        $slide.classList = `dot ${key === currentSlide ? 'active' : 'inactive'}`;
    });
}

/**
 * Show the next slide.
 */
function showNextSlide() {
    slideTo(currentSlide);
    currentSlide++;
}

// Run initialization functions when the window is fully loaded
window.onload = () => {
    if ($SLIDES) {
        initDots();
        initButtons();
        initIntervals();
    }
}