[y, fs] = audioread("input/Part_4/ball_bounce_brick_mono.wav");
figure;
plot(1:1000, y(1:1000), 'b')
xlabel('Sample number (only the first 1000)');
ylabel('y')
title('The input waveform')

spectrogram(y, 512, 256, 512, fs, 'yaxis');
title('Spectrogram of input signal')

saveas(gcf, 'ball bounce brick.png')