rgb = imread('p1_image1.png');
gray_image = rgb2gray(rgb);
[centers, radii] = imfindcircles(rgb, [35 45], 'ObjectPolarity','dark', 'Sensitivity', .95);
imshow(rgb)
h = viscircles(centers, radii);
