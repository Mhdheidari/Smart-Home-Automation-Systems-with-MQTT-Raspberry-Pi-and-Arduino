/*
   IoT Temperature and Light Control System

   This Arduino sketch implements a temperature and light control system
   using an analog temperature sensor, a light sensor, a motor, and an LED.

   The system operates as follows:
   - The temperature sensor measures the ambient temperature.
   - If the temperature falls below a threshold (26 degrees Celsius in this example),
     the motor is turned off.
   - If the temperature rises above the threshold, the motor is turned on.
   - The light sensor measures the ambient light level.
   - If the light level is below a threshold (100 in this example), the LED is turned off.
   - If the light level is above the threshold, the LED brightness is adjusted based on
     the light level.

   The system continuously monitors the temperature and light level, adjusts the motor
   and LED accordingly, and sends the data (temperature and light status) to the
   Serial Monitor for monitoring.

   Connections:
   - Temperature Sensor: A0
   - Motor Control Pin: 11
   - Light Sensor: A2
   - LED Control Pin: 6

   Author: Mohammad Heidari
   Date: July, 2023
*/

#define ANALOGREFVOLTAGE 5.00
int temperaturePin = A0;
int motorPin = 11;
int lightPin = A2;
int ledPin = 6;

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(motorPin, OUTPUT);
  Serial.begin(9600); // Initialize serial communication
}

void loop() {
  float temperature = getTemperature(temperaturePin);
  String Light = String(3);

  if (temperature < 26) {
    digitalWrite(motorPin, LOW); // Turn off the motor
  } else {
    digitalWrite(motorPin, HIGH); // Turn on the motor
  }

  int lightLevel = analogRead(lightPin);
  lightLevel = map(lightLevel, 0, 1023, 0, 255);

  if (lightLevel < 100) {
    analogWrite(ledPin, 0); // Turn off the LED completely
    Light = "OFF"; // Print "off" to the serial monitor
  } else {
    analogWrite(ledPin, lightLevel); // Set LED brightness based on the light level
    Light = "ON"; // Print "on" to the serial monitor
  }

  // Create an array and store the temperature and Light values
  String data[2] = {String(temperature), Light};

  // Print the values in the array on the same line
  for (int i = 0; i < 2; i++) {
    Serial.print(data[i]);
    if (i < 1) { // Don't print a comma after the last element
      Serial.print(", ");
    }
  }
  Serial.println(); // Print a newline character at the end of the line

  delay(500); // Wait for 1 second
}

float getTemperature(int pin) {
  float voltage = getVoltage(pin);
  float temperature = (voltage - 0.5) * 100.0;
  return temperature;
}

float getVoltage(int pin) {
  return (analogRead(pin) * ANALOGREFVOLTAGE / 1023.0);
}
