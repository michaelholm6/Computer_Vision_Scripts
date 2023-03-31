[y, fs] = audioread("input/Part_5/minecraft chest open.wav");
figure;
plot(1:1000, y(1:1000), 'b')
xlabel('Sample number (only the first 1000)');
ylabel('y')
title('The input waveform')

spectrogram(y, 512, 256, 512, fs, 'yaxis');
title('Spectrogram of input signal')

saveas(gcf, 'miencraft chest open.png')

%I recorded these video game sounds from minecraft. I used a software
%called audacity and recorded at a frequency of 44100 Hz. I varied the
%duration to be long enough to capture the entire sound in question. 
%To compute the spectrogram, I used a window of size 512, and overlap 
%of 256, and a number of points per window of 512. 
%I used a sampling frequency of 44100, and I plotted the frequencies
%along the Y axis. 