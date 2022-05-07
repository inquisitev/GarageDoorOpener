# GarageDoorOpener
Remote control of a garage door, Hoping to grow into a feature rich, budget friendly option.


## Hardware

### Parts List
[Piface digital 2](http://www.piface.org.uk/products/piface_digital_2/)

[Raspberry Pi 3B](https://www.raspberrypi.com/products/raspberry-pi-3-model-b/)

[Hall Effect Sensors (6pk)](https://www.amazon.com/gp/product/B01M8JCGSO/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&psc=1)

### Hook Up

Connect the garage door cable to the relay, Normally Open and Common. 

Connect one end of each hall effect sensor to 5v, and the other end to a digital terminal on the piface.

<img width="546" alt="Screen Shot 2022-05-07 at 2 09 03 PM" src="https://user-images.githubusercontent.com/44409350/167268515-bc6e9add-1738-43e6-8c79-981a641ef522.png">

## Running the Server
Just run `docker-compose up` to build all services

