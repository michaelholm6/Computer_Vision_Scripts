rgb = imread('p3_image3.png');
gray_image = rgb2gray(rgb);
binaryImage = imbinarize(gray_image, .3);
binaryImage = ~binaryImage(:,:,1);
binaryImage = bwareafilt(binaryImage, [50, 500]);
imshow(rgb)

numbers = ['6' '5' '4' '3' '2' '1'];
for number = numbers
    structuringElement = imread(append(number, '_gray.png'));
    structuringElement = imbinarize(structuringElement, .1);
    structuringElement = ~structuringElement(:,:,1);
    structuringElement = imresize(structuringElement, 1.7);
    if number == '3'
        structuringElement = imerode(structuringElement, strel('rectangle', [4 4]));
    else
        structuringElement = imerode(structuringElement, strel('rectangle', [3 3]));
    end
    erodedBinaryImage = imerode(binaryImage, structuringElement);
    [height, width] = size(erodedBinaryImage);
    for i = 1:height
        for j = 1:width
            if erodedBinaryImage(i, j) == 1
                text(j, i, number, 'Color', 'red', 'FontWeight', 'bold', 'FontSize', 20)
                deleteImage = imdilate(erodedBinaryImage, structuringElement);
                binaryImage = binaryImage - deleteImage;
            end
        end
    end
end
