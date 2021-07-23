BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "AdministrApp_cliente" (
	"id"	integer NOT NULL,
	"fecha_cliente"	date NOT NULL,
	"documento_cliente"	varchar(20) NOT NULL,
	"nombre_cliente"	varchar(100) NOT NULL,
	"apellido_cliente"	varchar(100) NOT NULL,
	"celular_cliente"	varchar(20) NOT NULL,
	"correo_cliente"	varchar(100) NOT NULL,
	"genero_cliente"	varchar(20) NOT NULL,
	"obs_cliente"	text,
	"perfil_cliente"	varchar(20) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "AdministrApp_inmueble" (
	"id"	integer NOT NULL,
	"gps_inmueble"	varchar(20) NOT NULL,
	"direccion_inmueble"	varchar(100) NOT NULL,
	"barrio_inmueble"	varchar(20) NOT NULL,
	"ciudad_inmueble"	varchar(20) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "AdministrApp_solicitud" (
	"id"	integer NOT NULL,
	"fechaInicia_solicitud"	date NOT NULL,
	"obsInicia_solicitud"	text NOT NULL,
	"fechaFinal_solicitud"	date,
	"obsFinal_solicitud"	text,
	"estado_solicitud"	varchar(20) NOT NULL,
	"id_instalacion_id"	bigint,
	"tipo_solicitud"	varchar(20),
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("id_instalacion_id") REFERENCES "AdministrApp_instalacion"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "AdministrApp_aporte" (
	"id"	integer NOT NULL,
	"fecha_aporte"	date NOT NULL,
	"valor_aporte"	integer NOT NULL,
	"obs_aporte"	text NOT NULL,
	"id_cliente_id"	bigint NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("id_cliente_id") REFERENCES "AdministrApp_cliente"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "AdministrApp_gastooperativo" (
	"id"	integer NOT NULL,
	"fecha_gastoOperativo"	date NOT NULL,
	"concepto_gastoOperativo"	varchar(20) NOT NULL,
	"obs_gastoOperativo"	text NOT NULL,
	"id_cliente_id"	bigint,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("id_cliente_id") REFERENCES "AdministrApp_cliente"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "AdministrApp_estado" (
	"id"	integer NOT NULL,
	"nombre_estado"	varchar(20) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "AdministrApp_estadoinstalacion" (
	"id"	integer NOT NULL,
	"fecha_estadoInstalacion"	date NOT NULL,
	"obs_estadoInstalacion"	text NOT NULL,
	"id_estado_id"	bigint,
	"id_instalacion_id"	bigint,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("id_estado_id") REFERENCES "AdministrApp_estado"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("id_instalacion_id") REFERENCES "AdministrApp_instalacion"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "AdministrApp_plan" (
	"id"	integer NOT NULL,
	"fecha_plan"	date NOT NULL,
	"nombre_plan"	varchar(100) NOT NULL,
	"valor_plan"	integer NOT NULL,
	"estado_plan"	varchar(20) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "AdministrApp_planinstalacion" (
	"id"	integer NOT NULL,
	"fecha_planInstalacion"	date NOT NULL,
	"id_instalacion_id"	bigint,
	"id_plan_id"	bigint,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("id_instalacion_id") REFERENCES "AdministrApp_instalacion"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("id_plan_id") REFERENCES "AdministrApp_plan"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "AdministrApp_pagoservicio" (
	"id"	integer NOT NULL,
	"fecha_pagoServicio"	date NOT NULL,
	"valor_pagoServicio"	integer NOT NULL,
	"obs_pagoServicio"	text,
	"id_instalacion_id"	bigint,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("id_instalacion_id") REFERENCES "AdministrApp_instalacion"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "AdministrApp_material" (
	"id"	integer NOT NULL,
	"fecha_material"	date NOT NULL,
	"nombre_material"	varchar(100) NOT NULL,
	"mac_material"	varchar(100) NOT NULL,
	"userPass_material"	varchar(100),
	"obs_material"	text NOT NULL,
	"estado_material"	varchar(20) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "AdministrApp_materialinstalacion" (
	"id"	integer NOT NULL,
	"fecha_materialInstalacion"	date NOT NULL,
	"obs_materialInstalacion"	text,
	"id_instalacion_id"	bigint,
	"id_material_id"	bigint,
	FOREIGN KEY("id_material_id") REFERENCES "AdministrApp_material"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("id_instalacion_id") REFERENCES "AdministrApp_instalacion"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "AdministrApp_instalacion" (
	"id"	integer NOT NULL,
	"fecha_instalacion"	date NOT NULL,
	"nad_instalacion"	varchar(20) NOT NULL,
	"ip_instalacion"	varchar(20) NOT NULL,
	"valor_instalacion"	integer NOT NULL,
	"obs_instalacion"	text NOT NULL,
	"id_cliente_id"	bigint,
	"id_inmueble_id"	bigint,
	FOREIGN KEY("id_inmueble_id") REFERENCES "AdministrApp_inmueble"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("id_cliente_id") REFERENCES "AdministrApp_cliente"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "AdministrApp_cliente" VALUES (1,'2021-07-21','123456','antonio','alarcon','654123','antonioalarcon@gmail.com','Femenino','','Cliente');
INSERT INTO "AdministrApp_cliente" VALUES (2,'2021-07-21','789654','beatriz','bueno','521456','beatriz@hotmaiol.com','Femenino','','Cliente');
INSERT INTO "AdministrApp_cliente" VALUES (3,'2021-07-21','11452','Miller','riaño','625487','miller@riano.com','Masculino','','Socio');
INSERT INTO "AdministrApp_cliente" VALUES (4,'2021-07-21','2345555','Edwing','Sierra','3325548','edwing@correo.com','Masculino','','Socio');
INSERT INTO "AdministrApp_cliente" VALUES (5,'2021-07-21','963258','maria','Marquez','45211','julian@hotmail.com','Femenino','','Empleado');
INSERT INTO "AdministrApp_cliente" VALUES (6,'2021-07-21','852311','carlos','castro','452111','carlos@gmail.com','Masculino','','Cliente');
INSERT INTO "AdministrApp_cliente" VALUES (7,'2021-07-21','135141','julian','blanco','1141445','julian@hotmail.com','Masculino','','Socio');
INSERT INTO "AdministrApp_inmueble" VALUES (1,'1.0000564, 17.021748','vivienda de Antonio','Palmas','Bucaramanga');
INSERT INTO "AdministrApp_inmueble" VALUES (2,'1.4400564, 17.021748','casa de beatriz','Mirador','Giron');
INSERT INTO "AdministrApp_solicitud" VALUES (1,'2021-07-22','Solicito instalación',NULL,'','Activo',3,'Instalación');
INSERT INTO "AdministrApp_aporte" VALUES (1,'2021-07-10',220000,'Arriendo local',4);
INSERT INTO "AdministrApp_aporte" VALUES (2,'2021-07-18',250000,'Ventana e instalación',3);
INSERT INTO "AdministrApp_gastooperativo" VALUES (1,'2021-07-05','conbustible','cemento para la ventana',3);
INSERT INTO "AdministrApp_estado" VALUES (1,'Activo');
INSERT INTO "AdministrApp_estado" VALUES (2,'En proceso');
INSERT INTO "AdministrApp_estado" VALUES (3,'Cerrado');
INSERT INTO "AdministrApp_estadoinstalacion" VALUES (1,'2021-07-13','Se requieren otros elementos,',2,1);
INSERT INTO "AdministrApp_estadoinstalacion" VALUES (2,'2021-07-22','se realizan pruebas quedando en funcionamiento',1,1);
INSERT INTO "AdministrApp_estadoinstalacion" VALUES (3,'2021-07-06','Ok, instalad',1,2);
INSERT INTO "AdministrApp_estadoinstalacion" VALUES (4,'2021-07-22','instalado correctamente',1,3);
INSERT INTO "AdministrApp_plan" VALUES (1,'2021-07-22','plan de 5 megas',40000,'Activo');
INSERT INTO "AdministrApp_plan" VALUES (2,'2021-07-22','plan de 10 megas',60000,'Activo');
INSERT INTO "AdministrApp_planinstalacion" VALUES (1,'2021-07-22',1,1);
INSERT INTO "AdministrApp_planinstalacion" VALUES (2,'2021-07-06',2,2);
INSERT INTO "AdministrApp_planinstalacion" VALUES (3,'2021-07-22',3,2);
INSERT INTO "AdministrApp_pagoservicio" VALUES (1,'2021-07-22',40000,'pendiente 10000',1);
INSERT INTO "AdministrApp_pagoservicio" VALUES (2,'2021-07-22',30000,'pendeinte 20000',2);
INSERT INTO "AdministrApp_pagoservicio" VALUES (3,'2021-07-22',20000,'',3);
INSERT INTO "AdministrApp_pagoservicio" VALUES (4,'2021-07-05',10000,'pago parcial',2);
INSERT INTO "AdministrApp_material" VALUES (1,'2021-07-22','cable drop de 2 hilos','sin','sin','sin','Activo');
INSERT INTO "AdministrApp_material" VALUES (2,'2021-07-22','nad de 16 puertos','sin','sin','sin','Activo');
INSERT INTO "AdministrApp_material" VALUES (3,'2021-07-22','modem','hdhd-kjf-jgds-peueu','user. admin','sin','Activo');
INSERT INTO "AdministrApp_materialinstalacion" VALUES (1,'2021-07-14','20 metros',1,1);
INSERT INTO "AdministrApp_materialinstalacion" VALUES (2,'2021-07-14','mac hdhd-kjf-jgds-peueu
pass user. admin',1,3);
INSERT INTO "AdministrApp_materialinstalacion" VALUES (3,'2021-07-22','Se deja nad en poste para el servicioo',1,2);
INSERT INTO "AdministrApp_materialinstalacion" VALUES (4,'2021-07-06','Mac
Pass
user',2,3);
INSERT INTO "AdministrApp_materialinstalacion" VALUES (5,'2021-07-06','80 metros',2,1);
INSERT INTO "AdministrApp_materialinstalacion" VALUES (6,'2021-07-22','25 metros',3,1);
INSERT INTO "AdministrApp_materialinstalacion" VALUES (7,'2021-07-22','mac
pass
user',3,3);
INSERT INTO "AdministrApp_instalacion" VALUES (1,'2021-07-22','el de la esquina','192.168.1.1',0,'80 mts de drop
20 conectores',5,2);
INSERT INTO "AdministrApp_instalacion" VALUES (2,'2021-07-22','otra nad','192.168.12.14',50000,'Se cobran 50.000 por estar muy lejos d ela zona',1,1);
INSERT INTO "AdministrApp_instalacion" VALUES (3,'2021-07-22','otra nad en otra esq','125.147.222.12',0,'sin pagos',6,2);
CREATE INDEX IF NOT EXISTS "AdministrApp_solicitud_id_instalacion_id_83a5d6a5" ON "AdministrApp_solicitud" (
	"id_instalacion_id"
);
CREATE INDEX IF NOT EXISTS "AdministrApp_aporte_id_cliente_id_eac2dabe" ON "AdministrApp_aporte" (
	"id_cliente_id"
);
CREATE INDEX IF NOT EXISTS "AdministrApp_gastooperativo_id_cliente_id_fba16236" ON "AdministrApp_gastooperativo" (
	"id_cliente_id"
);
CREATE INDEX IF NOT EXISTS "AdministrApp_estadoinstalacion_id_estado_id_5db9ccdb" ON "AdministrApp_estadoinstalacion" (
	"id_estado_id"
);
CREATE INDEX IF NOT EXISTS "AdministrApp_estadoinstalacion_id_instalacion_id_fb6ab762" ON "AdministrApp_estadoinstalacion" (
	"id_instalacion_id"
);
CREATE INDEX IF NOT EXISTS "AdministrApp_planinstalacion_id_instalacion_id_f36842a9" ON "AdministrApp_planinstalacion" (
	"id_instalacion_id"
);
CREATE INDEX IF NOT EXISTS "AdministrApp_planinstalacion_id_plan_id_23f9588f" ON "AdministrApp_planinstalacion" (
	"id_plan_id"
);
CREATE INDEX IF NOT EXISTS "AdministrApp_pagoservicio_id_instalacion_id_b6e097c1" ON "AdministrApp_pagoservicio" (
	"id_instalacion_id"
);
CREATE INDEX IF NOT EXISTS "AdministrApp_materialinstalacion_id_instalacion_id_e0310423" ON "AdministrApp_materialinstalacion" (
	"id_instalacion_id"
);
CREATE INDEX IF NOT EXISTS "AdministrApp_materialinstalacion_id_material_id_f00fb7d7" ON "AdministrApp_materialinstalacion" (
	"id_material_id"
);
CREATE INDEX IF NOT EXISTS "AdministrApp_instalacion_id_cliente_id_6e7e24f9" ON "AdministrApp_instalacion" (
	"id_cliente_id"
);
CREATE INDEX IF NOT EXISTS "AdministrApp_instalacion_id_inmueble_id_1fd47ecc" ON "AdministrApp_instalacion" (
	"id_inmueble_id"
);
COMMIT;
