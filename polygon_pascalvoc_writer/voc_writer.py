# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 10:30:17 2019

@author: EvitanRelta
Improved upon AndrewCarterUK's pascal-voc-writer. (https://github.com/AndrewCarterUK/pascal-voc-writer)
"""
from os import path as Path
from PIL import Image
from jinja2 import PackageLoader, Environment
from xml.sax.saxutils import escape

class VocWriter:
    def __init__(self, imageDir, annotationDir, imageName, depth=3, database='Unknown', segmented=0):
        environment = Environment(loader=PackageLoader('polygon_pascalvoc_writer','templates'),keep_trailing_newline=True)
        self.annotation_template = environment.get_template('annotation.xml')
        
        self.imageDir = imageDir        
        self.annotationDir = annotationDir
        self.imageName = imageName

        self.template_parameters = {
            'depth': depth,
            'database': escape(database),
            'segmented': segmented,
            'objects': []
        }
    
    def nextImage(self, imageName, depth=3, database='Unknown', segmented=0):
        self.imageName = imageName
        self.template_parameters = {
            'depth': depth,
            'database': escape(database),
            'segmented': segmented,
            'objects': []
        }
        

    def addBndBox(self, name, xmin, ymin, xmax, ymax, pose='Unspecified', truncated=0, difficult=0):
        self.template_parameters['objects'].append({
            'name': escape(name),
            'pose': escape(pose),
            'truncated': truncated,
            'difficult': difficult,
            'xmin': xmin,
            'ymin': ymin,
            'xmax': xmax,
            'ymax': ymax
        })
            
    def addPolygon(self, name, points, pose='Unspecified', truncated=0, difficult=0):
        self.template_parameters['objects'].append({
            'name': escape(name),
            'pose': escape(pose),
            'truncated': truncated,
            'difficult': difficult,
            'points': points,
            'xmin': min(points, key=lambda x:x[0])[0],
            'ymin': min(points, key=lambda x:x[1])[1],
            'xmax': max(points, key=lambda x:x[0])[0],
            'ymax': max(points, key=lambda x:x[1])[1]
        })

    def save(self):
        imagePath = Path.join(self.imageDir, self.imageName)
        imageWidth, imageHeight = self.getImageSize()
        _ = self.template_parameters
        _['filename'] = escape(Path.basename(self.imageName))
        _['folder'] = escape(Path.basename(Path.abspath(self.imageDir)[:-1]))
        _['path'] = escape(Path.abspath(imagePath))
        _['width'] = imageWidth
        _['height'] = imageHeight
        
        annotationName = Path.splitext(self.imageName)[0] + '.xml'
        annotationPath = Path.join(self.annotationDir, annotationName)
        with open(annotationPath, 'w') as file:
            content = self.annotation_template.render(**self.template_parameters)
            file.write(content)
    
    def getImageSize(self):
        imagePath = Path.join(self.imageDir, self.imageName)
        imageWidth, imageHeight = Image.open(imagePath).size
        return imageWidth, imageHeight
        
        
                    
                
            
