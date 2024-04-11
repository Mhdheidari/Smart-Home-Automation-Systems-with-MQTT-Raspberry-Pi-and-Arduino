/*
   Ultrasonic Distance Sensor with Buzzer Alarm

   This Arduino sketch implements an ultrasonic distance sensor with a buzzer alarm.
   The system uses an ultrasonic sensor to measure distance and a buzzer to
   produce an alarm sound when the distance is less than a certain threshold.

   The system operates as follows:
   - The ultrasonic sensor measures the distance to an object.
   - If the distance is greater than 10 cm, the system considers the door closed.
   - If the distance is less than or equal to 10 cm, the system considers the door open
     and activates the buzzer alarm.

   The distance measurements and door status (Open/Closed) are sent to the Serial Monitor
   for monitoring.

   Components:
   - Ultrasonic Sensor
   - Buzzer

   Pin Connections:
   - Trigger Pin of Sensor: 13
   - Echo Pin of Sensor: 8
   - Buzzer Pin: 12

   Author: Mohammad Heidari
   Date: July, 2023
*/

#include <NewPing.h>

#define TRIGGER_PIN  13  // Arduino pin tied to the trigger pin on the ultrasonic sensor.
#define ECHO_PIN     8   // Arduino pin tied to the echo pin on the ultrasonic sensor.
#define MAX_DISTANCE 200 // Maximum distance we want to ping for (in centimeters). Maximum sensor distance is rated at 400-500cm.
#define BUZZER_PIN   12  // Arduino pin connected to the buzzer.

NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE);  // NewPing setup of pins and maximum distance.

void setup() {
  pinMode(BUZZER_PIN, OUTPUT);  // Set the buzzer pin as an output
  Serial.begin(9600);  // Open the serial monitor at 115200 baud to see ping results.
}

void loop() {
  delay(50);  // Wait 50ms between pings (about 20 pings/sec). 29ms should be the shortest delay between pings.
  int distance = sonar.ping_cm();  // Send a ping and get the distance in cm
  String door = String(6);

  if (distance > 10) {
    door = "Closed";
  }
  else {
    door = "Open";
    alarm();  // Call the function to produce the beep sound
  }

  //Serial.print("Distance: ");
  //Serial.print(distance);  // Print the distance in cm

  Serial.println(String(distance)+","+ door);
  // Plot the distance on the Arduino plotter
  //Serial.print("Distance:");
  //Serial.println(distance);
  delay(300);
}

void alarm() {
  unsigned long startTime = millis();
  unsigned long duration = 1000;  // Duration of the alarm in milliseconds (10 seconds)

  int notes[] = {
    10,  // Note: C4
    1,   // Note: D4
    10,  // Note: C4
    1,   // Note: D4
    10,  // Note: C4
    1,   // Note: D4
    10,  // Note: C4
    1    // Note: D4
  };

  int durations[] = {
    100,  // Duration in milliseconds
    100,
    100,
    100,
    100,
    100,
    100,
    100
  };

  int numNotes = sizeof(notes) / sizeof(notes[0]);

  while (millis() - startTime < duration) {
    for (int i = 0; i < numNotes; i++) {
      int duration = durations[i];
      int note = notes[i];

      for (long t = 0; t < duration * 1000L; t += 1000 / note) {
        digitalWrite(BUZZER_PIN, HIGH);
        delayMicroseconds(1000 / note / 2);
        digitalWrite(BUZZER_PIN, LOW);
        delayMicroseconds(1000 / note / 2);
      }

      delay(duration);
    }
  }

  digitalWrite(BUZZER_PIN, LOW);  // Turn off the buzzer after the alarm finishes
}
