# Polygon Pascal VOC Writer

A simple python module to generate Pascal VOC XML image annotation files.
<br>Currently only supports bounding-boxes and polygons.

Improved upon AndrewCarterUK's [Pascal VOC Writer](https://github.com/AndrewCarterUK/pascal-voc-writer).

<br>

## Table of Contents

>- [Polygon Pascal VOC Writer](#Polygon-Pascal-VOC-Writer)
>- [Table of Contents](#Table-of-Contents)
>- [Example Execution](#Example-Execution)
>   - [For a single image](#For-a-single-image)
>   - [For a folder of images](#For-a-folder-of-images)

<br>

## Example Execution

### For a single image
> ###### [back to **_Contents_**](#Table-of-Contents)

Write annotation for `myImage.png` _(width: 100, height: 150)_ :

```python
images_dir = r"dir\images\"
annotations_dir = r"dir\annotations\"
image_name = "myImage.png"
writer = VocWriter(images_dir, annotations_dir, image_name)

# Rectangular bounding box
box_name = "myLabelBox"
xmin, ymin, xmax, ymax = 1, 2, 3, 4
writer.addBndBox(box_name, xmin, ymin, xmax, ymax)

# 1st polygon
polygon_1_name = "myPolygon"
vertices_1 = [
    [1, 2],
    [3, 4],
    [5, 6]
]
writer.addPolygon(polygon_1_name, vertices_1)

# 2nd polygon
polygon_2_name = "myPolygon"
vertices_2 = [
    [10, 20],
    [30, 40],
    [50, 60]
]
writer.addPolygon(polygon_2_name, vertices_2)

# Write to XML file in VOC format
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
    <object>
        <name>myPolygon</name>
        <pose>Unspecified</pose>
        <truncated>0</truncated>
        <difficult>0</difficult>
        <polygon>
            <x1>10</x1>
            <y1>20</y1>
            <x2>30</x2>
            <y2>40</y2>
            <x3>50</x3>
            <y3>60</y3>
        </polygon>
        <bndbox>
            <xmin>10</xmin>
            <ymin>20</ymin>
            <xmax>50</xmax>
            <ymax>60</ymax>
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
    {
        "image_name": "image1.png",
        "polygons": [
            [1, 2], [3, 4], [5, 6],
            [10, 20], [30, 40], [50, 60]
        ]
    },
    {
        "image_name": "image2.png",
        "polygons": [
            [7, 8], [9, 10], [11, 12],
            [70, 80], [90, 100], [110, 120]
        ]
    }
]
for annotation in list_of_annotations:
    # Clears the label data, then sets the image with
    # name matching annotation["image_name"] as the current working image.
    # Doesn't save the label data. Saving is done by writer.save()
    writer.nextImage(annotation["image_name"])  
    
    for polygon_vertices in annotation["polygons"]:
        writer.addPolygon("polygon_name", polygon_vertices)

    # Write to XML file in VOC format
    writer.save()
```

<br>

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
