from flask import Flask, render_template_string

app = Flask(__name__)

html = """

<!DOCTYPE html>
<html lang="en">
<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Rao Tula Ram Shooting Volleyball Ground</title>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:'Poppins',sans-serif;
    scroll-behavior:smooth;
}

body{
    background:#050816;
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

.bg
