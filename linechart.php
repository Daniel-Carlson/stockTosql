<!--- This is the acting "HTML" file that will display the chart --->

<HTML>
<HEAD>
<TITLE>Danny Stock App </TITLE>
<META NAME="Description" CONTENT="Write a one sentence description here.">
<META NAME="Keywords" CONTENT="Put your keywords here. Very important for many search engines.">
<META NAME="Author" CONTENT="Your Name Here">
<style>
.chart-container{
	height:50%;
	width: 50%;
}

</style>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.3/Chart.min.js" integrity="sha512-s+xg36jbIujB2S2VKfpGmlC3T5V2TF3lY48DX7u2r9XzGzgPsa6wTpOQA7J9iffvdeBN0q9tKzRxVxw1JviZPg==" crossorigin="anonymous"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<link href=>
</HEAD>
<BODY >

<div class="chart-container">
	<canvas id="line-chartcanvas"></canvas>
</div>

<!-- javascript-->
<script src="line-db-php.js"></script>
<br>
<br>

<div id="sum-container">
	
</div>


</BODY>
</HTML>
