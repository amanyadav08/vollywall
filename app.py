from flask import Flask, render_template_string

app = Flask(__name__)

html = """

<!DOCTYPE html>
<html lang="en">
<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Rao Tula Ram Shooting Volleyball Ground | Dhani Mehanda</title>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:'Poppins',sans-serif;
    scroll-behavior:smooth;
}

body{
    background:#0b1120;
    color:white;
    overflow-x:hidden;
}

/* Animated Background */

.bg{
    position:fixed;
    width:100%;
    height:100%;
    z-index:-1;
    overflow:hidden;
}

.bg span{
    position:absolute;
    width:20px;
    height:20px;
    background:rgba(250,204,21,0.15);
    animation:move 20s linear infinite;
    bottom:-100px;
    border-radius:50%;
}

.bg span:nth-child(1){left:10%;width:80px;height:80px;}
.bg span:nth-child(2){left:25%;width:50px;height:50px;animation-duration:12s;}
.bg span:nth-child(3){left:40%;width:120px;height:120px;}
.bg span:nth-child(4){left:60%;width:70px;height:70px;}
.bg span:nth-child(5){left:80%;width:100px;height:100px;}

@keyframes move{
    0%{
        transform:translateY(0) rotate(0deg);
        opacity:1;
    }

    100%{
        transform:translateY(-1200px) rotate(720deg);
        opacity:0;
    }
}

/* Navbar */

nav{
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:25px 8%;
    position:fixed;
    width:100%;
    top:0;
    z-index:1000;
    background:rgba(0,0,0,0.4);
    backdrop-filter:blur(12px);
}

.logo{
    font-size:34px;
    font-weight:800;
    color:#facc15;
}

nav ul{
    display:flex;
    gap:35px;
    list-style:none;
}

nav ul li a{
    color:white;
    text-decoration:none;
    transition:0.3s;
    font-size:18px;
}

nav ul li a:hover{
    color:#facc15;
}

/* Hero */

.hero{
    min-height:100vh;
    background:
    linear-gradient(rgba(0,0,0,0.7),rgba(0,0,0,0.8)),
    url('https://images.unsplash.com/photo-1547347298-4074fc3086f0?q=80&w=2070&auto=format&fit=crop') center/cover;
    display:flex;
    justify-content:center;
    align-items:center;
    text-align:center;
    padding:40px;
}

.hero-content{
    max-width:1100px;
    animation:fadeIn 2s ease;
}

.hero h1{
    font-size:85px;
    color:#facc15;
    margin-bottom:30px;
    line-height:1.2;
}

.hero p{
    font-size:26px;
    color:#e2e8f0;
    line-height:2;
    margin-bottom:45px;
}

.btn{
    display:inline-block;
    padding:18px 45px;
    background:#facc15;
    color:black;
    text-decoration:none;
    border-radius:50px;
    font-size:20px;
    font-weight:700;
    transition:0.4s;
}

.btn:hover{
    transform:scale(1.08);
    background:white;
}

/* Fade Animation */

@keyframes fadeIn{
    from{
        opacity:0;
        transform:translateY(60px);
    }

    to{
        opacity:1;
        transform:translateY(0);
    }
}

/* Common */

section{
    padding:120px 8%;
}

.title{
    text-align:center;
    font-size:60px;
    color:#facc15;
    margin-bottom:80px;
}

/* About */

.about{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:60px;
    align-items:center;
}

.about img{
    width:100%;
    border-radius:25px;
    transition:0.5s;
}

.about img:hover{
    transform:scale(1.03);
}

.about-text{
    font-size:22px;
    line-height:2;
    color:#cbd5e1;
}

/* Passion Section */

.passion{
    background:linear-gradient(135deg,#111827,#1e293b);
    padding:80px;
    border-radius:35px;
    text-align:center;
}

.passion h2{
    font-size:55px;
    color:#facc15;
    margin-bottom:30px;
}

.passion p{
    font-size:24px;
    line-height:2;
    color:#e2e8f0;
}

/* Cards */

.cards{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(280px,1fr));
    gap:35px;
}

.card{
    background:#1e293b;
    padding:40px;
    border-radius:25px;
    transition:0.4s;
}

.card:hover{
    transform:translateY(-12px);
    background:#334155;
}

.card h3{
    color:#facc15;
    margin-bottom:20px;
    font-size:30px;
}

.card p{
    line-height:1.9;
    color:#cbd5e1;
}

/* Gallery */

.gallery{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(300px,1fr));
    gap:30px;
}

.gallery img{
    width:100%;
    border-radius:25px;
    transition:0.5s;
}

.gallery img:hover{
    transform:scale(1.05);
}

/* Stats */

.stats{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
    gap:30px;
}

.stat{
    background:#1e293b;
    padding:50px;
    border-radius:25px;
    text-align:center;
}

.stat h2{
    font-size:65px;
    color:#facc15;
}

.stat p{
    margin-top:15px;
    font-size:24px;
}

/* Footer */

footer{
    background:#020617;
    padding:40px;
    text-align:center;
    color:#94a3b8;
    margin-top:50px;
}

/* Responsive */

@media(max-width:900px){

    .hero h1{
        font-size:50px;
    }

    .hero p{
        font-size:18px;
    }

    .about{
        grid-template-columns:1fr;
    }

    nav{
        flex-direction:column;
        gap:20px;
    }

}

</style>

</head>

<body>

<div class="bg">
<span></span>
<span></span>
<span></span>
<span></span>
<span></span>
</div>

<nav>

<div class="logo">RTR Volleyball</div>

<ul>
<li><a href="#">Home</a></li>
<li><a href="#">Ground</a></li>
<li><a href="#">Players</a></li>
<li><a href="#">Gallery</a></li>
<li><a href="#">Contact</a></li>
</ul>

</nav>

<section class="hero">

<div class="hero-content">

<h1>Rao Tula Ram Shooting Volleyball Ground</h1>

<p>

Dhani Mehanda ki mitti se nikla Haryana ka volleyball junoon.

Yaha bacche, jawaan aur buzurg sab volleyball ke liye ek jaise passionate hain.
Har sham ground par energy, crowd aur sportsmanship ka alag hi mahaul hota hai.

Door door se log matches dekhne aur support karne aate hain.

</p>

<a href="#" class="btn">Welcome To Dhani Mehanda</a>

</div>

</section>

<section>

<h2 class="title">About Our Ground</h2>

<div class="about">

<img src="https://lh3.googleusercontent.com/p/AF1QipO45PQL9amjaVjbCPF21TDihk4YQe6LZgR6ENEm=w203-h152-k-no">

<div class="about-text">

Rao Tula Ram Shooting Volleyball Ground Dhani Mehanda sirf ek ground nahi,
balki Haryana ke volleyball lovers ki pehchaan hai.

Yaha har roz practice hoti hai, tournaments hote hain aur gaon ke talented players ko mauka diya jata hai.

Yeh ground discipline, passion aur sports spirit ka symbol ban chuka hai.

</div>

</div>

</section>

<section>

<div class="passion">

<h2>Volleyball Is Our Passion</h2>

<p>

Yaha ke bachon ke liye volleyball sirf game nahi — ek emotion hai.

Subah practice, shaam matches aur tournament nights ka atmosphere dekhne layak hota hai.

Ground par energy, crowd aur Haryana ki asli sports culture feel hoti hai.

</p>

</div>

</section>

<section>

<h2 class="title">What Makes Us Special</h2>

<div class="cards">

<div class="card">
<h3>Village Unity</h3>
<p>Yaha har age ke log volleyball ko support karte hain aur players ka hausla badhate hain.</p>
</div>

<div class="card">
<h3>Strong Passion</h3>
<p>Ground par players ka passion aur dedication dekhkar bahar ke log bhi impress ho jaate hain.</p>
</div>

<div class="card">
<h3>Tournament Atmosphere</h3>
<p>Night tournaments aur cheering crowd is ground ki asli pehchaan hai.</p>
</div>

<div class="card">
<h3>Future Players</h3>
<p>Gaon ke talented players ko training aur exposure diya jata hai.</p>
</div>

</div>

</section>

<section>

<h2 class="title">Ground Gallery</h2>

<div class="gallery">

<img src="https://lh3.googleusercontent.com/p/AF1QipNlpYKmE-znr3AsX1SUdyGV-KLjY2lzv4dyPFlT=w203-h114-k-no">

<img src="https://lh3.googleusercontent.com/p/AF1QipO45PQL9amjaVjbCPF21TDihk4YQe6LZgR6ENEm=w203-h152-k-no">

<img src="https://lh3.googleusercontent.com/gps-cs-s/APNQkAF-vTk0MkLG8P-HKsNz5I8BUqMjNVEkHCWwSVLq0dX6mCraHYAzf_Zn7MRFPM3ieGjNVyYvqkX6AcSF6OfUpqhCMoJ0QrOIjY87WywF8anw_vr2BvsmWoceFsz2__CRiE2XTcsVaxSu9PY=w203-h273-k-no">

</div>

</section>

<section>

<h2 class="title">Our Achievements</h2>

<div class="stats">

<div class="stat">
<h2>100+</h2>
<p>Tournaments Played</p>
</div>

<div class="stat">
<h2>500+</h2>
<p>Players Connected</p>
</div>

<div class="stat">
<h2>1000+</h2>
<p>Supporters</p>
</div>

<div class="stat">
<h2>24x7</h2>
<p>Sports Passion</p>
</div>

</div>

</section>

<footer>

© 2026 Rao Tula Ram Shooting Volleyball Ground | Dhani Mehanda Haryana

</footer>

</body>
</html>

"""

@app.route('/')
def home():
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
