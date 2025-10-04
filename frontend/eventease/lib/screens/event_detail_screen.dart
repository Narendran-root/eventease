import 'package:flutter/material.dart';
import '../models/event.dart';
import '../api/api_service.dart';
import 'package:fluttertoast/fluttertoast.dart';

class EventDetailScreen extends StatelessWidget {
  final Event event;
  final ApiService api = ApiService();

  EventDetailScreen({required this.event});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(event.title)),
      body: Padding(
        padding: EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(event.title, style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold)),
            SizedBox(height: 8),
            Text("${event.date} • ${event.location}", style: TextStyle(fontSize: 16)),
            SizedBox(height: 16),
            Text(event.description),
            SizedBox(height: 20),
            ElevatedButton(
              child: Text("Book Event"),
              onPressed: () async {
                bool success = await api.bookEvent(event.id);
                if (success) {
                  Fluttertoast.showToast(msg: "Booking Successful");
                } else {
                  Fluttertoast.showToast(msg: "Booking Failed / Already Booked");
                }
              },
            )
          ],
        ),
      ),
    );
  }
}
