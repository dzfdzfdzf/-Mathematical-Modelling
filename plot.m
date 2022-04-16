%XY=xlsread('C:/Users/asus/Desktop/data2/20161017 (27)..xlsx')
XY=importdata('C:/Users/asus/Desktop/20161017 (27)2.txt')
lon = XY(:,2); %经度
lat = XY(:,3); %纬度
webmap OpenStreetMap;
wmline(lat, lon, 'Color', 'b', 'Width', 3);
for i=1:length(lat)
    wmmarker(lat(i),lon(i),'IconScale',0.4);
end;
