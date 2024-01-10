# AirBnB_clone

**First step: Write a command interpreter to manage your AirBnB objects.**

This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

> Each task is linked and will help you to:
>
> - put in place a parent class (called `BaseModel`) to take care of the initialization, serialization and deserialization of your future instances
> - create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
> - create all classes used for AirBnB (`User`, `State`, `City`, `Place`…) that inherit from `BaseModel`
> - create the first abstracted storage engine of the project: File storage.
> - create all unittests to validate all our classes and storage engine

## BaseModel class diagram

```mermaid
classDiagram

	class BaseModel {
		+String id
		+Datetime created_at
		+Datetime updated_at
		+save()
		+to_dict()
	}

	class State {
		+String name
	}

	class City {
		+String state_id
		+String name
	}

	class Amenity {
		+String name
	}

	class Place {
		+String city_id
		+String user_id
		+String name
		+String description
		+Integer number_rooms
		+Integer number_bathrooms
		+Integer max_guest
		+Integer price_by_night
		+Float latitude
		+Float longitude
		+List~String~ amenity_ids
	}

	class Review {
		+String place_id
		+String user_id
		+String text
	}

	Protocol <|-- IBaseModel
	IBaseModel <|-- BaseModel
	BaseModel <|-- User
	BaseModel <|-- State
	BaseModel <|-- City
	BaseModel <|-- Place
	BaseModel <|-- Amenity
	BaseModel <|-- Review

	class FileStorage {
		-String file_path
		-Dict objects
		+all()
		+new(obj)
		+save()
		+reload()
	}

	class SansStorage {
		+String name
		-get_name()
	}
	FileStorage <|-- SansStorage

	Protocol <|-- IFileStorage
	IFileStorage <|-- FileStorage
```