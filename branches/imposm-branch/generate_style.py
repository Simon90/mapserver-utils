#!/usr/bin/env python


maxscales = {
   0:99999999999,
   1:332808204,
   2:166404102,
   3:83202051,
   4:41601025,
   5:20800512,
   6:10400256,
   7:5200128,
   8:2600064,
   9:1300032,
   10:650016,
   11:325008,
   12:162504,
   13:81252,
   14:40626,
   15:20313,
   16:10156,
   17:5078,
   18:2539
}
minscales = {
   0:332808204,
   1:166404102,
   2:83202051,
   3:41601025,
   4:20800512,
   5:10400256,
   6:5200128,
   7:2600064,
   8:1300032,
   9:650016,
   10:325008,
   11:162504,
   12:81252,
   13:40626,
   14:20313,
   15:10156,
   16:5078,
   17:2539,
   18:0
}

defaults = {
   'dbconnection': {0:'"host=localhost dbname=osm user=osm password=osm port=5432"'},
   'font': {0:'"sc"'},
   'boldfont': {0:'"scb"'},
   'lbl_clr': {0:"0 0 0"},
   'lbl_size': {0:7},
   'lbl_ol_clr':{0:"255 255 255"},
   'lbl_ol_width':{0:2},
   'water_clr': {0:'"#B3C6D4"'},
   'water_font': {0:'"sc"'},
   'water_lbl_size':{0:7},
   'water_lbl_clr':{0:'"#6B94B0"'},
   'water_lbl_ol_clr':{0:'255 255 255'},
   'water_lbl_ol_width':{0:2},

};

vars= {
   'maxscale':maxscales,
   'minscale':minscales,
   'db_connection': defaults['dbconnection'],
   'ocean_clr': defaults['water_clr'],
   'land_clr': {
      0:'"#E8E6E1"'
   },
   'forest_clr': {
      0:'"#C2D1B2"'
   },
   'residential_clr': {
      0:'"#E3DED4"'
   },
   'industrial_clr': {
      0:'"#d1d1d1"'
   },
   'hospital_clr': {
      0:'"#E6C8C3"'
   },
   'education_clr': {
      0:'"#DED1AB"'
   },
   'cemetery_clr': {
      0:'"#d1d1d1"'
   },
   'park_clr': {
      0:'"#DCDCB4"'
   },
   'waterarea_clr':defaults['water_clr'],
   'river_clr':defaults['water_clr'],
   'stream_clr':defaults['water_clr'],
   'canal_clr':defaults['water_clr'],


   'display_canal_lbl' : {0:0, 6:1},
   'canal_font': defaults['water_font'],
   'canal_lbl_size': defaults['water_lbl_size'],
   'canal_lbl_clr': defaults['water_lbl_clr'],
   'canal_lbl_ol_clr': defaults['water_lbl_ol_clr'],
   'canal_lbl_ol_width': defaults['water_lbl_ol_width'],

   'display_stream_lbl' : {0:0, 6:1},
   'stream_font': defaults['water_font'],
   'stream_lbl_size': defaults['water_lbl_size'],
   'stream_lbl_clr': defaults['water_lbl_clr'],
   'stream_lbl_ol_clr': defaults['water_lbl_ol_clr'],
   'stream_lbl_ol_width': defaults['water_lbl_ol_width'],

   'display_river_lbl' : {0:0, 6:1},
   'river_font': defaults['water_font'],
   'river_lbl_size': defaults['water_lbl_size'],
   'river_lbl_clr': defaults['water_lbl_clr'],
   'river_lbl_ol_clr': defaults['water_lbl_ol_clr'],
   'river_lbl_ol_width': defaults['water_lbl_ol_width'],

   'display_waterarea_lbl' : {0:0, 6:1},
   'waterarea_font': defaults['water_font'],
   'waterarea_lbl_size': defaults['water_lbl_size'],
   'waterarea_lbl_clr': defaults['water_lbl_clr'],
   'waterarea_lbl_ol_clr': defaults['water_lbl_ol_clr'],
   'waterarea_lbl_ol_width': defaults['water_lbl_ol_width'],

   'display_industrial_lbl' : {0:0, 6:1},
   'industrial_font': defaults['font'],
   'industrial_lbl_size': defaults['lbl_size'],
   'industrial_lbl_clr': defaults['lbl_clr'],
   'industrial_lbl_ol_clr': defaults['lbl_ol_clr'],
   'industrial_lbl_ol_width': defaults['lbl_ol_width'],

   'display_residential_lbl' : {0:0, 6:1},
   'residential_font': defaults['font'],
   'residential_lbl_size': defaults['lbl_size'],
   'residential_lbl_clr': defaults['lbl_clr'],
   'residential_lbl_ol_clr': defaults['lbl_ol_clr'],
   'residential_lbl_ol_width': defaults['lbl_ol_width'],

   'display_park_lbl' : {0:0, 6:1},
   'park_font': defaults['font'],
   'park_lbl_size': defaults['lbl_size'],
   'park_lbl_clr': defaults['lbl_clr'],
   'park_lbl_ol_clr': defaults['lbl_ol_clr'],
   'park_lbl_ol_width': defaults['lbl_ol_width'],

   'display_hospital_lbl' : {0:0, 6:1},
   'hospital_font': defaults['font'],
   'hospital_lbl_size': defaults['lbl_size'],
   'hospital_lbl_clr': defaults['lbl_clr'],
   'hospital_lbl_ol_clr': defaults['lbl_ol_clr'],
   'hospital_lbl_ol_width': defaults['lbl_ol_width'],

   'display_education_lbl' : {0:0, 6:1},
   'education_font': defaults['font'],
   'education_lbl_size': defaults['lbl_size'],
   'education_lbl_clr': defaults['lbl_clr'],
   'education_lbl_ol_clr': defaults['lbl_ol_clr'],
   'education_lbl_ol_width': defaults['lbl_ol_width'],

   'display_pedestrian_lbl' : {0:0, 6:1},
   'pedestrian_font': defaults['font'],
   'pedestrian_lbl_size': defaults['lbl_size'],
   'pedestrian_lbl_clr': defaults['lbl_clr'],
   'pedestrian_lbl_ol_clr': defaults['lbl_ol_clr'],
   'pedestrian_lbl_ol_width': defaults['lbl_ol_width'],

   'display_cemetery_lbl' : {0:0, 6:1},
   'cemetery_font': defaults['font'],
   'cemetery_lbl_size': defaults['lbl_size'],
   'cemetery_lbl_clr': defaults['lbl_clr'],
   'cemetery_lbl_ol_clr': defaults['lbl_ol_clr'],
   'cemetery_lbl_ol_width': defaults['lbl_ol_width'],

   'land_data': {
      0:'"data/TM_WORLD_BORDERS-0.3.shp"',
      3:'"data/shoreline_300"',
      7:'"data/processed_p"'
   },
   'land_epsg': {
      0:'"+init=epsg:4326"',
      3:'"+init=epsg:900913"',
   },
   'motorway_clr': {
      0:'"#ffffff"'
   },
   'motorway_width': {
      0:1,
      1:0.5
   },
   'motorway_lbl_clr': {
      0:'"#ffffff"'
   },
   'trunk_clr': {
      0:'"#ffffff"'
   },
   'trunk_width': {
      0:'"#ffffff"'
   },
   'trunk_lbl_clr': {
      0:'"#ffffff"'
   },
   'primary_clr': {
      0:'"#ffffff"'
   },
   'primary_width': {
      0:'"#ffffff"'
   },
   'primary_lbl_clr': {
      0:'"#ffffff"'
   },
   'secondary_clr': {
      0:'"#ffffff"'
   },
   'secondary_width': {
      0:'"#ffffff"'
   },
   'secondary_lbl_clr': {
      0:'"#ffffff"'
   },
   'tertiary_clr': {
      0:'"#ffffff"'
   },
   'tertiary_width': {
      0:'"#ffffff"'
   },
   'tertiary_lbl_clr': {
      0:'"#ffffff"'
   },
   'other_clr': {
      0:'"#ffffff"'
   },
   'other_width': {
      0:'"#ffffff"'
   },
   'other_lbl_clr': {
      0:'"#ffffff"'
   },
   'pedestrian_clr': {
      0:'"#ffffff"'
   },
   'pedestrian_width': {
      0:'"#ffffff"'
   },
   'pedestrian_lbl_clr': {
      0:'"#ffffff"'
   },
   'track_clr': {
      0:'"#ffffff"'
   },
   'track_width': {
      0:'"#ffffff"'
   },
   'track_lbl_clr': {
      0:'"#ffffff"'
   },
   'path_clr': {
      0:'"#ffffff"'
   },
   'path_width': {
      0:'"#ffffff"'
   },
   'path_lbl_clr': {
      0:'"#ffffff"'
   },
   'railway_clr': {
      0:'"#ffffff"'
   },
   'railway_width': {
      0:'"#ffffff"'
   },
   'railway_inner_clr': {
      0:'"#ffffff"'
   },
   'railway_inner_width': {
      0:'"#ffffff"'
   },
   'railway_inner_pattern': {
      0:'"#ffffff"'
   },
   'landusage_data': {
      0:'"geometry from (select geometry ,osm_id, type, name from OSM_PREFIX_landusages \
      where type in (\'forest\',\'residential\')\
      order by z_order asc) as foo using unique osm_id using srid=OSM_SRID"',
      6:'"geometry from (select geometry ,osm_id, type, name from OSM_PREFIX_landusages \
      where type in (\'forest\',\'pedestrian\',\'cemetery\',\'industrial\',\'commercial\',\
      \'brownfield\',\'residential\',\'school\',\'college\',\'university\',\
      \'military\',\'park\',\'golf_course\',\'hospital\',\'parking\')\
      order by z_order asc) as foo using unique osm_id using srid=OSM_SRID"'
   },
   'border_data': {
      0: '"data/boundaries.shp"'
   },
   'display_border_2': {
      0:1
   },
   'display_border_2_outer': {
      0:0,
      6:1
   },
   'border_2_clr': {
      0:'"#CDCBC6"'
   },
   'border_2_width': {
      0:'5'
   },
   'border_2_inner_clr': {
      0:'"#CDCBC6"',
      5:'"#8d8b8d"'
   },
   'border_2_inner_width': {
      0:'0.5',
      5:'1'
   },
   'border_2_inner_pattern': {
      0:''
   },
   #         'display_border_4': {
   #            0:0,
   #            6:1
   #         },
   #         'display_border_4_outer': {
   #            0:0,
   #            7:1
   #         },
   #         'border_4_clr': {
   #            0:'"#CDCBC6"'
   #         },
   #         'border_4_width': {
   #            0:'5',
   #            8:'6'
   #         },
   #         'border_4_inner_clr': {
   #            0:'"#8d8b8d"'
   #         },
   #         'border_4_inner_width': {
   #            0:'0.5',
   #            7:'1'
   #         },
   #         'border_4_inner_pattern': {
   #            0:'',
   #            7:'PATTERN 2 2 END'
   #         },
   #         'display_border_6': {
   #            0:0,
   #            7:1
   #         },
   #         'display_border_6_outer': {
   #            0:0,
   #            9:1
   #         },
   #         'border_6_clr': {
   #            0:'"#CDCBC6"'
   #         },
   #         'border_6_width': {
   #            0:'5',
   #            13:'7'
   #         },
   #         'border_6_inner_clr': {
   #            0:'"#8d8b8d"'
   #         },
   #         'border_6_inner_width': {
   #            0:'0.5',
   #            9:1
   #         },
   #         'border_6_inner_pattern': {
   #            0:'',
   #            9:'PATTERN 2 2 END'
   #         },
   #         'display_border_8': {
   #            0:0,
   #            11:1
   #         },
   #         'display_border_8_outer': {
   #            0:0,
   #            13:1
   #         },
   #         'border_8_clr': {
   #            0:'"#CDCBC6"'
   #         },
   #         'border_8_width': {
   #            0:'5'
   #         },
   #         'border_8_inner_clr': {
   #            0:'"#8d8b8d"'
   #         },
   #         'border_8_inner_width': {
   #            0:'0.5',
   #            14:'1'
   #         },
   #         'border_8_inner_pattern': {
   #            0:'',
   #            13:'PATTERN 2 2 END'
   #         },
   'display_waterways': {
      0:0,
      6:1
   },
   'river_width': {
      0:0,
      6:0.15,
      7:0.25,
      8:0.5,
      9:1,
      11:2,
      13:3,
      15:4,
      16:5,
      17:6,
      18:7
   },
   'stream_width': {
      0:0,
      10:0.5,
      12:1,
      14:2
   },
   'canal_width': {
      0:0,
      10:0.5,
      12:1,
      14:2
   },
   'waterways_data': {
      0:'"geometry from (select geometry, osm_id, type, name from OSM_PREFIX_waterways where type=\'river\') as foo using unique osm_id using srid=OSM_SRID"',
      10:'"geometry from (select geometry, osm_id, type, name from OSM_PREFIX_waterways) as foo using unique osm_id using srid=OSM_SRID"'
   },
   'places_data': {
      0: '"geometry from (select * from OSM_PREFIX_places where name is not NULL order by population asc nulls first) as foo using unique osm_id using srid=OSM_SRID"'
   },
   'display_capitals': {
      0:1
   },
   'display_capital_symbol': {
      0:1,
      10:0
   },
   'capital_lbl_size': {
      0:8,
      10:10,
      12:12,
      14:18

   },
   'capital_size': {
      0:6
   },
   'capital_fg_size': {
      0:2
   },
   'capital_ol_clr': {
      0:'"#000000"'
   },
   'capital_fg_clr': {
      0:"0 0 0"
   },
   'capital_clr': {
      0:"255 0 0"
   },
   'capital_font': defaults['font'],
   'capital_lbl_clr': defaults['lbl_clr'],
   'capital_lbl_ol_clr': defaults['lbl_ol_clr'],
   'capital_lbl_ol_width':defaults['lbl_ol_width'],
   'display_cities': {
      0:0,
      5:1
   },
   'display_city_symbol': {
      0:1,
      10:0
   },
   'city_lbl_size': {
      0:7,
      10:8,
      12:10,
      14:14
   },
   'city_size': {
      0:5
   },
   'city_ol_clr': {
      0:'"#000000"'
   },
   'city_clr': {
      0:"200 200 200"
   },
   'city_font': defaults['font'],
   'city_lbl_clr': defaults['lbl_clr'],
   'city_lbl_ol_clr': defaults['lbl_ol_clr'],
   'city_lbl_ol_width':defaults['lbl_ol_width'],
   
   'display_towns': {
      0:0,
      5:1
   },
   'display_town_symbol': {
      0:1,
      10:0
   },
   'town_font': defaults['font'],
   'town_lbl_clr': defaults['lbl_clr'],
   'town_lbl_ol_clr': defaults['lbl_ol_clr'],
   'town_lbl_ol_width':defaults['lbl_ol_width'],
   'town_lbl_size': {
      0:7,
      10:8,
      12:10,
      14:14
   },
   'town_size': {
      0:5
   },
   'town_ol_clr': {
      0:'"#000000"'
   },
   'town_clr': {
      0:"200 200 200"
   },
   'village_font': defaults['font'],
   'village_lbl_clr': defaults['lbl_clr'],
   'village_lbl_ol_clr': defaults['lbl_ol_clr'],
   'village_lbl_ol_width':defaults['lbl_ol_width'],
   'display_villages': {
      0:0,
      5:1
   },
   'display_village_symbol': {
      0:1,
      10:0
   },
   'village_lbl_size': {
      0:7,
      10:8,
      12:10,
      14:14
   },
   'village_size': {
      0:5
   },
   'village_ol_clr': {
      0:'"#000000"'
   },
   'village_clr': {
      0:"200 200 200"
   },


   'hamlet_font': defaults['font'],
   'hamlet_lbl_clr': defaults['lbl_clr'],
   'hamlet_lbl_ol_clr': defaults['lbl_ol_clr'],
   'hamlet_lbl_ol_width': defaults['lbl_ol_width'],
   'display_hamlets': {
      0:0,
      5:1
   },
   'display_hamlet_symbol': {
      0:1,
      10:0
   },
   'hamlet_lbl_size': {
      0:7,
      10:8,
      12:10,

   },
   'hamlet_size': {
      0:5
   },
   'hamlet_ol_clr': {
      0:'"#000000"'
   },
   'hamlet_clr': {
      0:"200 200 200"
   }

}

import sys

if sys.argv[1] == "-s":
   print "###### level 0 ######"
   for k,v in vars.iteritems():
      print "#define _%s0 %s"%(k,v[0])

   for i in range(1,19):
      print
      print "###### level %d ######"%(i)
      for k,v in vars.iteritems():
         if not v.has_key(i):
            print "#define _%s%d _%s%d"%(k,i,k,i-1)
         else:
            print "#define _%s%d %s"%(k,i,v[i])

if sys.argv[1] == "-l":
   level = sys.argv[2]
   for k,v in vars.iteritems():
      print "#undef _%s"%(k)

   for k,v in vars.iteritems():
      print "#define _%s _%s%s"%(k,k,level)
