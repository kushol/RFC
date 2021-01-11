# template for the home page
root_template = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Welcome to Random Forest Classifier</title>
	<script src="/static/classifier_web.js"></script>    
</head>

<body>
<h1>Welcome to Random Forest Classifier</h1>
<img src="/static/demo.jpg" width="600" height="120" />
<p>Please choose a dataset file in CSV format and then apply the classifier.</p>

<form name="fileUploadForm" action="/" method="post" enctype="multipart/form-data" onsubmit="return validateForm()">  
  <input type="file" name="data" />
  <input type="submit" name="submit" value="Apply Classifier" />
</form>

</body>
</html>
    """

# template for the result page
result_template = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Welcome to Random Forest Classifier</title>
    <script src="/static/classifier_web.js"></script>
	<link rel="stylesheet" type="text/css" href="/static/classifier_web.css">    
</head>

<body>
<h1>Welcome to Random Forest Classifier</h1>  
<img src="/static/demo.jpg" width="600" height="120" />
<p>Please choose a dataset file in CSV format and then apply the classifier.</p>

<form name="fileUploadForm" action="/" method="post" enctype="multipart/form-data" onsubmit="return validateForm()">  
  <input type="file" name="data" />
  <input type="submit" name="submit" value="Apply Classifier" />
</form>

<br />

<div>
<table>
<tr>
    <th colspan="2">Chosen dataset information</th>
</tr>
<tr>
    <td>File:</td>
    <td>{{file_name}}</td>
</tr>
<tr>
    <td>Total Data:</td>
    <td>{{data_count}}</td>
</tr>    
<tr>
    <td>Features:</td>
    <td>{{features}}</td>
</tr>
<tr>
    <td>Targets:</td>
    <td>{{targets}}</td>
</tr>
<tr>
    <td>Accuracy:</td>
    <td>{{accuracy}}</td>
</tr>
</table>
</div>

<br /><br />

{{!result_trees}}

</body>
</html>
    """

