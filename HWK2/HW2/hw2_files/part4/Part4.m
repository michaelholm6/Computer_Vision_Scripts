clear
unedited = imread('image_part4a.png');
seLetter = imread('../../letter_cutouts/A.png');
binary = imbinarize(unedited, .9);
binary = ~binary(:,:,1);
se = imbinarize(seLetter, .9);
se = se(:,:,1);
eroded = imerode(binary, se);
eroded = bwareafilt(eroded, [0,1]);
eroded = imdilate(eroded, se);
eroded = ~eroded;
eroded = ~bwareafilt(eroded, [0,100000]);
edited = unedited;
size = [size(eroded, 1), size(eroded, 2)];
for i=1:size(1)
    for j = 1:size(2)
        if eroded(i, j) == 0
            edited(i,j,:) = [255, 0 ,0];
        end
    end
end
figure, imshow(edited)