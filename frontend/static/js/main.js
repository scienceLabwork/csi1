let timeline = document.getElementById("timeline");
let timeline2 = document.getElementById("timeline2");


let day1 = document.getElementById("day1");
let day2 = document.getElementById("day2");



day1.addEventListener("click", function() {
    if (timeline.style.display === "none") {
        timeline.style.display = "block";
        timeline2.style.display = "none";
        day1.classList.add("active");
        day2.classList.remove("active");
    } else {
        timeline.style.display = "block";
        timeline2.style.display = "none";
        day1.classList.add("active");
        day2.classList.remove("active");
    }
});
day2.addEventListener("click", function() {
    if (timeline2.style.display === "none") {
        timeline2.style.display = "block";
        timeline.style.display = "none";
        day2.classList.add("active");
        day1.classList.remove("active");
    } else {
        timeline2.style.display = "block";
        timeline.style.display = "none";
        day2.classList.add("active");
        day1.classList.remove("active");
    }
});


// when smooth scrolling is enabled, scroll to section with hash with more 15 px as the nav bar is 15 px high

if (document.querySelector(".navbar").classList.contains("navbar-smooth-scroll")) {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth',
                block: "start",
                inline: "nearest"
            });
        });
    });
}
