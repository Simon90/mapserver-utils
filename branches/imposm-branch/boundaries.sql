drop table if exists tbt_tmp_rings;


create table tbt_tmp_rings (id serial, admin_level smallint, geometry geometry);

insert into tbt_tmp_rings(admin_level,geometry) 
   SELECT admin_level, ST_Collect(ST_ExteriorRing(geometry)) AS geometry 
   FROM (
      SELECT admin_level, osm_id, (ST_Dump(geometry)).geom As geometry
      FROM osm_new_admin) As foo
   GROUP BY admin_level,osm_id;


insert into tbt_tmp_rings (admin_level,geometry) 
   select admin_level,st_collect(geom)
      from
      (select admin_level, ST_InteriorRingN(geom, generate_series(1, ST_NumInteriorRing(geom))) as geom
         from 
         (select admin_level,
            st_geometryN(geom, generate_series(1, st_numgeometries(geom))) as geom
            from
            (select admin_level, geometry as geom from osm_new_admin) as foo) as bar) as baz group by admin_level;

create index tbt_tmp_rings_idx on tbt_tmp_rings using gist(geometry);
drop table if exists tom_bnd_2;
drop table if exists tom_bnd_4;
drop table if exists tom_bnd_6;
drop table if exists tom_bnd_8;

create table tom_bnd_2 as (
   select c1.id, st_intersection(c1.geometry,c2.geometry) as geometry
   from tbt_tmp_rings c1, tbt_tmp_rings c2
   where c1.geometry && c2.geometry and c1.id!=c2.id and c1.admin_level=2 and c2.admin_level=2
);
create table tom_bnd_4 as (
   select c1.id, st_intersection(c1.geometry,c2.geometry) as geometry
   from tbt_tmp_rings c1, tbt_tmp_rings c2
   where c1.geometry && c2.geometry and c1.id!=c2.id and c1.admin_level=4 and c2.admin_level=4
);
create table tom_bnd_6 as (
   select c1.id, st_intersection(c1.geometry,c2.geometry) as geometry
   from tbt_tmp_rings c1, tbt_tmp_rings c2
   where c1.geometry && c2.geometry and c1.id!=c2.id and c1.admin_level=6 and c2.admin_level=6
);
create table tom_bnd_8 as (
   select c1.id, st_intersection(c1.geometry,c2.geometry) as geometry
   from tbt_tmp_rings c1, tbt_tmp_rings c2
   where c1.geometry && c2.geometry and c1.id!=c2.id and c1.admin_level=8 and c2.admin_level=8
);


