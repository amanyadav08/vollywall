from flask import Flask, render_template_string

app = Flask(__name__)

html = """

<!DOCTYPE html>
<html lang="en">
<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Dhani Mehanda Shooting Volleyball Club</title>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:'Poppins',sans-serif;
}

body{
    background:#0f172a;
    color:white;
    overflow-x:hidden;
}

/* Navbar */

nav{
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:25px 8%;
    background:rgba(0,0,0,0.5);
    backdrop-filter:blur(10px);
    position:fixed;
    width:100%;
    top:0;
    z-index:1000;
}

.logo{
    font-size:35px;
    font-weight:800;
    color:#facc15;
}

nav ul{
    display:flex;
    gap:30px;
    list-style:none;
}

nav ul li a{
    text-decoration:none;
    color:white;
    font-size:18px;
    transition:0.3s;
}

nav ul li a:hover{
    color:#facc15;
}

/* Hero Section */

.hero{
    height:100vh;
    background:
    linear-gradient(rgba(0,0,0,0.6),rgba(0,0,0,0.8)),
    url('https://images.unsplash.com/photo-1547347298-4074fc3086f0?q=80&w=2070&auto=format&fit=crop') center/cover;
    display:flex;
    justify-content:center;
    align-items:center;
    text-align:center;
    padding:40px;
}

.hero-content{
    max-width:1000px;
    animation:fadeIn 2s ease;
}

.hero h1{
    font-size:80px;
    color:#facc15;
    margin-bottom:25px;
}

.hero p{
    font-size:24px;
    line-height:1.8;
    color:#e2e8f0;
    margin-bottom:40px;
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

/* Animation */

@keyframes fadeIn{
    from{
        opacity:0;
        transform:translateY(50px);
    }

    to{
        opacity:1;
        transform:translateY(0);
    }
}

/* Sections */

section{
    padding:120px 8%;
}

.section-title{
    text-align:center;
    font-size:55px;
    color:#facc15;
    margin-bottom:70px;
}

/* About */

.about{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:50px;
    align-items:center;
}

.about img{
    width:100%;
    border-radius:25px;
}

.about-text{
    font-size:22px;
    line-height:2;
    color:#cbd5e1;
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
    font-size:28px;
}

.card p{
    color:#cbd5e1;
    line-height:1.8;
}

/* Gallery */

.gallery{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(300px,1fr));
    gap:30px;
}

.gallery img{
    width:100%;
    border-radius:20px;
    transition:0.4s;
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
    font-size:60px;
    color:#facc15;
}

.stat p{
    margin-top:15px;
    font-size:22px;
}

/* Contact */

.contact{
    background:#1e293b;
    padding:70px;
    border-radius:30px;
    text-align:center;
}

.contact h2{
    font-size:50px;
    color:#facc15;
    margin-bottom:30px;
}

.contact p{
    font-size:22px;
    margin-bottom:15px;
    color:#cbd5e1;
}

/* Footer */

footer{
    background:#020617;
    padding:30px;
    text-align:center;
    color:#94a3b8;
}

/* Responsive */

@media(max-width:900px){

    .hero h1{
        font-size:45px;
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

<nav>

<div class="logo">DMSVC</div>

<ul>
<li><a href="#">Home</a></li>
<li><a href="#">Team</a></li>
<li><a href="#">Gallery</a></li>
<li><a href="#">Achievements</a></li>
<li><a href="#">Contact</a></li>
</ul>

</nav>

<section class="hero">

<div class="hero-content">

<h1>Dhani Mehanda Shooting Volleyball Club</h1>

<p>

Professional Shooting Volleyball Club of Haryana.
Training Young Players and Participating in National Level Tournaments.

</p>

<a href="#" class="btn">Join Our Team</a>

</div>

</section>

<section>

<h2 class="section-title">About Club</h2>

<div class="about">

<img src="https://images.unsplash.com/photo-1517649763962-0c623066013b?q=80&w=2070&auto=format&fit=crop">

<div class="about-text">

Dhani Mehanda Shooting Volleyball Club is one of the fastest growing volleyball clubs in Haryana.

Our mission is to train young athletes with professional coaching and sports discipline.

We participate in district, state and national level volleyball tournaments and help players build successful sports careers.

</div>

</div>

</section>

<section>

<h2 class="section-title">Our Facilities</h2>

<div class="cards">

<div class="card">
<h3>Professional Coaching</h3>
<p>Experienced volleyball trainers with national level experience.</p>
</div>

<div class="card">
<h3>Daily Practice</h3>
<p>Morning and evening volleyball training sessions.</p>
</div>

<div class="card">
<h3>Tournament Support</h3>
<p>Participation in district and national tournaments.</p>
</div>

<div class="card">
<h3>Fitness Training</h3>
<p>Strength and stamina development for athletes.</p>
</div>

</div>

</section>

<section>

<h2 class="section-title">Tournament Gallery</h2>

<div class="gallery">

<img src="https://images.unsplash.com/photo-1546519638-68e109498ffc?q=80&w=2070&auto=format&fit=crop">

<img src="https://images.unsplash.com/photo-1517649763962-0c623066013b?q=80&w=2070&auto=format&fit=crop">

<img src="https://images.unsplash.com/photo-1521412644187-c49fa049e84d?q=80&w=2070&auto=format&fit=crop">

</div>

</section>

<section>

<h2 class="section-title">Our Achievements</h2>

<div class="stats">

<div class="stat">
<h2>50+</h2>
<p>Tournaments Played</p>
</div>

<div class="stat">
<h2>20+</h2>
<p>Trophies Won</p>
</div>

<div class="stat">
<h2>200+</h2>
<p>Players Trained</p>
</div>

<div class="stat">
<h2>10+</h2>
<p>State Level Players</p>
</div>

</div>

</section>

<section>

<div class="contact">

<h2>Contact Us</h2>

<p>📍 Dhani Mehanda, Haryana</p>
<p>📞 +91 XXXXX XXXXX</p>
<p>📧 volleyballclub@gmail.com</p>

</div>

</section>

<footer>

© 2026 Dhani Mehanda Shooting Volleyball Club

</footer>

</body>
</html>

"""

@app.route('/')
def home():
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
