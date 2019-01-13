<head>
  <style>
    p {font-family: Arial;}
    .class_name {font-family: Arial}
  <style>
</head>

======
<body>
  <p style="font-family: Arial;">
  </p>
</body>

=====
<style_file.css>
p {font-family: Arial; }
      ---
<head>
  <link href="./style.css" type="text/css" rel="stylesheet" >
</head>

=======

note:
(*) id attribute : is for anchor element <a> to jump internally to that page section
(*) class attribute : is for [css style] to target certain <div>

================
class attribute :
* use space to separate attributes
* <p class="class_1 class_2 class_3">
================
css selector:
* tag_name { }
* .class_name {}
* #id_name {}
* id > tag.class(h1.class) > class > tag  
* nested element:
       .class tag ==> .main-list li  (li: <li> item)
===========
如果同時有兩個class 衝突， 【在style.css 裡，排在最下面的那個（furthest down）will win out】
