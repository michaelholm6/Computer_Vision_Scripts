clear
unedited = imread('image_part3a.png');
figure, imshow(unedited)
binary = imbinarize(unedited, .9);
binary = ~binary(:,:,1);
se = strel('line', 60, 0);
dilation = imdilate(binary, se);
se = strel('line', 60, 90);
dilation = imdilate(dilation, se);
bw2 = bwareaopen(dilation, 100000);
result = ~(bw2 .* binary);
topCoordinate = inf;
bottomCoordinate = 0;
leftCoordinate = inf;
rightCoordinate = 0;
size = [size(result, 1), size(result, 2)];
for i=1:size(1)
    for j = 1:size(2)
        if result(i, j) == 0 && i < topCoordinate
            topCoordinate = i;
        end
        if result(i, j) == 0 && i > bottomCoordinate
            bottomCoordinate = i;
        end
        if result(i, j) == 0 && j < leftCoordinate
            leftCoordinate = j;
        end
        if result(i, j) == 0 && j > rightCoordinate
            rightCoordinate = j;
        end
    end
end
cropRectangle = [leftCoordinate, topCoordinate, rightCoordinate-leftCoordinate bottomCoordinate-topCoordinate];
result = imcrop(result, cropRectangle);
figure, imshow(result)