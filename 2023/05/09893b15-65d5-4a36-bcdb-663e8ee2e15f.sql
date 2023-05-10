create database if not exists car;
use car;
create external table car_2019712(
province string comment '省',
month int comment '月',
city string comment '市',
district string comment '区县',
year int comment '年',
model string comment '车辆型号',
manufacturer string comment '制造商',
brand string comment '品牌',
vehicletype string comment '车辆类型',
ownership string comment '所有权',
nature string comment '使用性质',
quantity int comment '数量',
enginemodel string comment '发动机型号',
displacement int comment '排量',
power int comment '功率',
fuel string comment '燃料种类',
length1 int comment '车长',
width1 int comment '车宽',
height1 int comment '车高',
length2 int comment '厢长',
width2 int comment '厢宽',
height2 int comment '厢高',
numberofaxles int comment '轴数',
wheelbase int comment '轴距',
frontwheelbase int comment '前轮距',
tirespecification string comment '轮胎规格',
tirenumber int comment '轮胎数',
totalquality int comment '总质量',
completequality int comment '整备质量',
approvedquality int comment '核定载质量',
approvedpassenger string comment '核定载客',
tractionquality int comment '准牵引质量',
chassisenterprise string comment '底盘企业',
chassisbrand string comment '底盘品牌',
chassismodel string comment '底盘型号',
engineenterprise string comment '发动机企业',
vehiclename string comment '车辆名称',
age int comment '年龄',
gender string comment '性别'
)
comment 'this is the raw data'
row format delimited
fields terminated by ','
location '/cars';