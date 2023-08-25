# Import the dependencies.
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################



# reflect an existing database into a new model

engine = create_engine("sqlite///Resources/hawaii.sqlite")
Base = automap_base()

# reflect the tables

Base.prepare(autoload_with=engine)

# Save references to each table

Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB

session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"Precipitation: /api/v1.0/precipitation<br/>"
        f"Stations list: /api/v1.0/stations<br/>"
        f"Temperature from most recent year: /api/v1.0/tobs<br/>"
        f"Temperature from start date: /api/v1.0/<start><br/>"
        f"Temperature from start to end date: /api/v1.0/<start>/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    
    sel = [Measurement.date,
       Measurement.prcp]
    results = session.query(*sel).all()
    
    precipitation = []
    for date, prcp in results:
        prcp_dict = {}
        prcp_dict["Date"] = date
        prcp_dict["Precipitation"] = prcp
        precipitation.append(prcp_dict)  
    
    return jsonify(precipitation)
    
@app.route("/api/v1.0/stations")
def stations():
    
    sel = [Station.station,
           Station.name,
           Station.latitude,
           Station.longitude,
           Station.elevation]
    results = session.query(*sel).all()
    
    stations = []
    for station, name, lat, lon, el in results:
        station_dict = {}
        station_dict["Station"] = station
        station_dict["Name"] = name
        station_dict["Latitude"] = lat
        station_dict["Longitude"] = lonconda 
        station_dict["Elevation"] = el
        stations.append(station_dict)
    
    return jsonify(stations)     
    
@app.route("/api/v1.0/tobs")
def tobs():
    
    most_recent = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    query_date = most_recent - dt.timedelta(days=365)
    
    sel = [Measurement.date,
       Measurement.tobs]
    results = session.query(*sel).filter(Measurement.date >= query_date).all()
    
    tobs = []
    for date, tobs in results:
        tobs_dict = {}
        tobs_dict["Date"] = date
        tobs_dict["Tobs"] = tobs
        tobs.append(tobs_dict)
    
    return jsonify(tobs)   
       
@app.route("/api/v1.0/<start>")
def temp_start(start):
    
    sel = [func.min(Measurement.tobs),
           func.avg(Measurement.tobs),
           func.max(Measurement.tobs)]
    results = session.query(*sel).filter(Measurement.date >= start).all()
    
    tobs = []
    for min, avg, max in results:
        tobs_dict = {}
        tobs_dict["Min"] = min
        tobs_dict["Average"] = avg
        tobs_dict["Max"] = max
        tobs.append(tobs_dict)
    
    return jsonify(tobs)  
        
@app.route("/api/v1.0/<start>/<end>")
def temp_start_end(start, end):
    
    sel = [func.min(Measurement.tobs),
           func.avg(Measurement.tobs),
           func.max(Measurement.tobs)]
    results = session.query(*sel).filter(Measurement.date >= start).filter(Measurement.date >= start).all() 
     
    tobs = []
    for min, avg, max in results:
        tobs_dict = {}
        tobs_dict["Min"] = min
        tobs_dict["Average"] = avg
        tobs_dict["Max"] = max
        tobs.append(tobs_dict)
    
    return jsonify(tobs)  
    
    
    
session.close()        