from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>STEM Reach</title>

<style>
*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

body{
    background:#030609;
    color:#f5f5f5;
    font-family:Arial, sans-serif;
    overflow-x:hidden;
}

/* NAVBAR */
nav{
    height:100px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    padding:0 7%;
    border-bottom:1px solid #18202b;
    background:#05080c;
}

.logo{
    display:flex;
    align-items:center;
    gap:15px;
    font-size:21px;
    font-weight:bold;
}

.logo-icon{
    width:55px;
    height:55px;
    border-radius:20px;
    display:flex;
    align-items:center;
    justify-content:center;
    color:#27d5ff;
    background:linear-gradient(135deg,#123f4b,#14182e);
}

nav ul{
    display:flex;
    list-style:none;
    gap:50px;
}

nav a{
    color:#9ba0aa;
    text-decoration:none;
    font-size:17px;
    font-weight:bold;
}

nav a:hover{
    color:#25cfff;
}

/* HERO */
.hero{
    min-height:570px;
    padding:100px 7%;
    position:relative;
    background:
    radial-gradient(circle at 50% 10%,#07343b 0%,transparent 35%),
    linear-gradient(#030609,#030609);
}

.tag{
    display:inline-block;
    border:1px solid #1b2a34;
    border-radius:30px;
    padding:12px 20px;
    color:#b8bdc6;
    margin-bottom:35px;
}

.dot{
    color:#22cfff;
}

.hero h1{
    font-size:68px;
    max-width:650px;
    line-height:1.05;
    letter-spacing:-2px;
}

.blue{
    color:#23c8f1;
}

.hero p{
    color:#969ca8;
    font-size:21px;
    line-height:1.8;
    max-width:680px;
    margin-top:30px;
}

.buttons{
    display:flex;
    gap:20px;
    margin-top:35px;
}

button{
    border:none;
    padding:18px 35px;
    border-radius:30px;
    font-size:17px;
    font-weight:bold;
    cursor:pointer;
}

.primary{
    background:#20bfe2;
    color:#061016;
}

.secondary{
    background:#090d16;
    color:#d8dce3;
    border:1px solid #202838;
}

/* STATS */
.stats{
    padding:40px 7%;
}

.stat-card,
.card,
.cta{
    background:
    linear-gradient(120deg,rgba(7,15,27,.98),rgba(4,8,14,.98));
    border:1px solid #182433;
    border-radius:28px;
    box-shadow:
    0 0 50px rgba(0,180,220,.05);
}

.stat-card{
    padding:35px;
    margin:25px 0;
}

.stat-number{
    font-size:50px;
    color:#28cef3;
    font-weight:bold;
}

.stat-card p{
    margin-top:12px;
    color:#969ca8;
    font-size:18px;
}

/* PROGRAM */
.section{
    padding:80px 7%;
}

.section-title{
    display:flex;
    justify-content:space-between;
    align-items:center;
    margin-bottom:35px;
}

.section-title h2{
    font-size:42px;
}

.small-text{
    color:#939aa7;
    letter-spacing:2px;
}

.card{
    padding:35px;
    margin:25px 0;
}

.number{
    display:inline-flex;
    align-items:center;
    justify-content:center;
    width:65px;
    height:65px;
    border-radius:20px;
    background:#07303a;
    color:#24cef4;
    font-size:22px;
    margin-right:25px;
}

.card-content{
    display:inline-block;
    vertical-align:middle;
    width:80%;
}

.card h3{
    font-size:25px;
}

.card p{
    color:#979eaa;
    margin-top:12px;
    font-size:18px;
}

.link{
    color:#26c8ee;
    text-decoration:none;
    font-weight:bold;
    font-size:18px;
    display:inline-block;
    margin-top:25px;
}

/* PROJECTS */
.project{
    display:flex;
    align-items:center;
    gap:25px;
}

.project-icon{
    width:100px;
    height:100px;
    border-radius:20px;
    background:
    radial-gradient(circle,#0b6b74,#05080d 70%);
}

.project h3{
    font-size:25px;
}

.project p{
    color:#8f96a2;
}

/* CTA */
.cta{
    margin:60px 7% 100px;
    padding:50px;
}

.cta h2{
    font-size:42px;
}

.cta p{
    color:#969ca8;
    margin:20px 0 30px;
    font-size:19px;
    line-height:1.7;
}

/* MOBILE */
@media(max-width:700px){

    nav{
        padding:0 25px;
        height:85px;
    }

    nav ul{
        display:none;
    }

    .hero{
        padding:70px 32px;
    }

    .hero h1{
        font-size:48px;
    }

    .hero p{
        font-size:18px;
    }

    .buttons{
        flex-wrap:wrap;
    }

    .section,
    .stats{
        padding:50px 30px;
    }

    .section-title h2{
        font-size:34px;
    }

    .card{
        padding:25px;
    }

    .number{
        margin-bottom:15px;
    }

    .card-content{
        width:100%;
    }

    .cta{
        margin:30px;
        padding:35px;
    }

    .cta h2{
        font-size:34px;
    }
}
</style>
</head>

<body>

<nav>
    <div class="logo">
        <div class="logo-icon">S</div>
        STEM Reach
    </div>

    <ul>
        <li><a href="#home">Home</a></li>
        <li><a href="#about">About</a></li>
        <li><a href="#program">Program</a></li>
        <li><a href="#projects">Projects</a></li>
        <li><a href="#register">Register</a></li>
    </ul>
</nav>


<section class="hero" id="home">

    <div class="tag">
        <span class="dot">●</span> &nbsp;10-week free cohort
    </div>

    <h1>
        Where curiosity<br>
        <span class="blue">becomes craft.</span>
    </h1>

    <p>
        A free, immersive STEM outreach program for high school,
        middle school, and college students.
        Learn by building, lead by doing.
    </p>

    <div class="buttons">
        <button class="primary">Apply now</button>
        <button class="secondary">Explore</button>
    </div>

</section>


<section class="stats">

    <div class="stat-card">
        <div class="stat-number">10</div>
        <p>Weeks of hands-on building</p>
    </div>

    <div class="stat-card">
        <div class="stat-number" style="color:#a99cff">3</div>
        <p>Grade levels, one table</p>
    </div>

    <div class="stat-card">
        <div class="stat-number" style="color:white">0</div>
        <p>Cost, always free</p>
    </div>

</section>


<section class="section" id="program">

    <div class="section-title">
        <h2>The Program</h2>
        <span class="small-text">Leadership + learning</span>
    </div>

    <div class="card">
        <span class="number">01</span>

        <div class="card-content">
            <h3>Robotics & Systems</h3>
            <p>
                Assemble and program a team project across
                collaborative sprint cycles.
            </p>
        </div>
    </div>


    <div class="card">
        <span class="number" style="background:#17172c;color:#aaa0ff">
            02
        </span>

        <div class="card-content">
            <h3>Data & Design</h3>
            <p>
                Turn real datasets into meaningful dashboards,
                research, and creative projects.
            </p>
        </div>
    </div>


    <div class="card">
        <span class="number" style="background:#20242d;color:white">
            03
        </span>

        <div class="card-content">
            <h3>Lead & Pitch</h3>
            <p>
                Build leadership skills and present your work
                through a final public demonstration.
            </p>
        </div>
    </div>

    <a class="link" href="#">
        View full 10-week schedule →
    </a>

</section>


<section class="section" id="projects">

    <div class="section-title">
        <h2>Featured Projects</h2>
        <a class="link" href="#">See all</a>
    </div>

    <div class="card project">

        <div class="project-icon"></div>

        <div>
            <h3>Hydro-Sense Sensor</h3>
            <p>Cohort 4 &nbsp;•&nbsp; Sensors</p>
        </div>

    </div>


    <div class="card project">

        <div class="project-icon"
        style="background:
        radial-gradient(circle,#244b7a,#080a10 70%)"></div>

        <div>
            <h3>Air-Quality Atlas</h3>
            <p>Cohort 3 &nbsp;•&nbsp; Data</p>
        </div>

    </div>

</section>


<section class="cta" id="register">

    <h2>Reserve your seat</h2>

    <p>
        Cohort 5 opens soon. Free for all students.
        Apply before the deadline and start building.
    </p>

    <button class="primary">
        Apply now
    </button>

</section>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)