# Polygon Pascal VOC Writer

A simple python module to generate Pascal VOC xml annotation files. Currently only supports boundingBoxes and polygons.

Improved upon AndrewCarterUK's pascal-voc-writer. (Link: <https://github.com/AndrewCarterUK/pascal-voc-writer>)

## Table of Contents

- [Polygon Pascal VOC Writer](#Polygon-Pascal-VOC-Writer)
- [Table of Contents](#Table-of-Contents)
- [Example Execution](#Example-Execution)
    - [For a single image](#For-a-single-image)
    - [For a folder of images](#For-a-folder-of-images)


## Example Execution

### For a single image
> ###### [back to **_Contents_**](#Table-of-Contents)

Write annotation for `myImage.png` _(width: 100, height: 150)_ :

```python
images_dir = r"dir\images\"
annotations_dir = r"dir\annotations\"
image_name = "myImage.png"
writer = VocWriter(images_dir, annotations_dir, image_name)

box_name = "myLabelBox"
xmin, ymin, xmax, ymax = 1, 2, 3, 4
writer.addBndBox(box_name, xmin, ymin, xmax, ymax)

polygon_name = "myPolygon"
vertices = [
    [1, 2],
    [3, 4],
    [5, 6]
]
writer.addPolygon("myPolygon", vertices)

writer.save()
```

<br>

Output file, `dir\annotation\myImage.xml` :

```xml
<annotation>
    <folder>images</folder>    
    <filename>myImage.png</filename>
    <path>dir\images\myImage.png</path>
    <source>
        <database>Unknown</database>
    </source>
    <size>
        <width>100</width>
        <height>150</height>
        <depth>3</depth>
    </size>
    <segmented>0</segmented>
    <object>
        <name>myLabelBox</name>
        <pose>Unspecified</pose>
        <truncated>0</truncated>
        <difficult>0</difficult>
        <bndbox>
            <xmin>1</xmin>
            <ymin>2</ymin>
            <xmax>3</xmax>
            <ymax>4</ymax>
        </bndbox>
    </object>
    <object>
        <name>myPolygon</name>
        <pose>Unspecified</pose>
        <truncated>0</truncated>
        <difficult>0</difficult>
        <polygon>
            <x1>1</x1>
            <y1>2</y1>
            <x2>3</x2>
            <y2>4</y2>
            <x3>5</x3>
            <y3>6</y3>
        </polygon>
        <bndbox>
            <xmin>1</xmin>
            <ymin>2</ymin>
            <xmax>5</xmax>
            <ymax>6</ymax>
        </bndbox>
    </object>
</annotation>
```

<br>

### For a folder of images
> ###### [back to **_Contents_**](#Table-of-Contents)

Write annotation for `image1.png` and `image2.png` :
```python
images_dir = r"dir\images\"
annotations_dir = r"dir\annotations\"
writer = VocWriter(images_dir, annotations_dir, "")

list_of_annotations = [
    {"image_name" : "image1.png",
     "polygon" : [[1, 2], [3, 4], [5, 6]]},
    {"image_name" : "image2.png",
     "polygon" : [[7, 8], [9, 10], [11, 12]]}
]
for annotation in list_of_annotations:
    writer.nextImage(annotation["image_name"])
    writer.addPolygon("polygon_name", annotation["polygon"])
    writer.save()
```
Resulting directories: 
```
dir
├── images
|   ├── image1.png
|   └── image2.png
└── annotations
    ├── image1.xml
    ├── image2.xml
```