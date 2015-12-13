curl -XPUT "elastic.tlr.io:9200/weather" -d '

{
  "mappings" : {
    "default" : {
      "dynamic" : "false",      
      "properties" : {
        "clouds" : {
          "properties" : {
            "all" : {
              "type" : "long"
            }
          }
        },
        "location" : {
          "type" : "geo_point"
        },
        "country" : {
          "type" : "string",
          "index" : "not_analyzed"
        },
        "dt_es" : {
          "type" : "date",
          "format" : "strict_date_optional_time||epoch_millis"
        },
        "id" : {
          "type" : "long"
        },
        "main" : {
          "properties" : {
            "grnd_level" : {
              "type" : "double"
            },
            "humidity" : {
              "type" : "long"
            },
            "pressure" : {
              "type" : "double"
            },
            "sea_level" : {
              "type" : "double"
            },
            "temp" : {
              "type" : "double"
            },
            "temp_kf" : {
              "type" : "double"
            },
            "temp_max" : {
              "type" : "double"
            },
            "temp_min" : {
              "type" : "double"
            }
          }
        },
        "city" : {
          "type" : "string",
          "index" : "not_analyzed"            
        },
        "rain" : {
          "properties" : {
            "3h" : {
              "type" : "long"
            }
          }
        },
        "snow" : {
          "properties" : {
            "3h" : {
              "type" : "double"
            }
          }
        },
        "sys" : {
          "properties" : {
            "pod" : {
              "type" : "string"
            }
          }
        },
        "weather" : {
          "properties" : {
            "description" : {
              "type" : "string"                
            },
            "icon" : {
              "type" : "string"
            },
            "id" : {
              "type" : "long"
            },
            "main" : {
              "type" : "string",
              "index" : "not_analyzed"                
            }
          }
        },
        "wind" : {
          "properties" : {
            "deg" : {
              "type" : "double"
            },
            "speed" : {
              "type" : "double"
            }
          }
        }
      }
    }
  }
}


'
