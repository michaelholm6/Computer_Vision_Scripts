%horizontal lines
unedited = imread('image_part1a.png');
binary = imbinarize(unedited, .9);
binary = ~binary(:,:,1);
figure, imshow(binary)
se = strel('line', 61, 0);
horizontalLines = imerode(binary, se);
horizontalLines = imdilate(horizontalLines, se);
figure, imshow(horizontalLines)

%vertical lines
unedited = imread('image_part1b.png');
binary = imbinarize(unedited, .9);
binary = ~binary(:,:,1);
figure, imshow(binary)
se = strel('line', 61, 90);
verticalLines = imerode(binary, se);
verticalLines = imdilate(verticalLines, se);
figure, imshow(verticalLines)