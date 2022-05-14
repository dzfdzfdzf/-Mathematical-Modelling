%XY=xlsread('C:/Users/asus/Desktop/raw_format_xlsx/20161017 (287).xlsx')
%XY=xlsread('C:/Users/asus/Desktop/DeleteFlyPoint_xlsx/20161017 (287).xlsx');
%XY=xlsread('C:/Users/asus/Desktop/DeleteFlyPoint_xlsx/20161017 (133).xlsx');
%XY=xlsread('C:/Users/asus/Desktop/loss_xlsx/20161017 (8).xlsx');
XY=importdata('C:/Users/asus/Desktop/dp/20161017 (8).txt');


lon = XY(:,2); %经度
lat = XY(:,3); %纬度
webmap OpenStreetMap;
wmline(lat, lon, 'Color', 'b', 'Width', 3);
for i=1:length(lat)
    wmmarker(lat(i),lon(i),'IconScale',0.4);
end
