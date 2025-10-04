import 'package:flutter/material.dart';
import 'screens/login_screen.dart';

void main() {
  runApp(EventEaseApp());
}

class EventEaseApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'EventEase',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: LoginScreen(),
    );
  }
}
