import 'package:flutter/material.dart';
import '../api/api_service.dart';
import '../models/booking.dart';

class BookingsScreen extends StatefulWidget {
  @override
  _BookingsScreenState createState() => _BookingsScreenState();
}

class _BookingsScreenState extends State<BookingsScreen> {
  final ApiService api = ApiService();
  List<Booking> bookings = [];
  bool loading = true;

  @override
  void initState() {
    super.initState();
    loadBookings();
  }

  Future<void> loadBookings() async {
    final fetchedBookings = await api.fetchBookings();
    setState(() {
      bookings = fetchedBookings;
      loading = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("My Bookings")),
      body: loading
          ? Center(child: CircularProgressIndicator())
          : bookings.isEmpty
              ? Center(child: Text("No bookings yet"))
              : ListView.builder(
                  itemCount: bookings.length,
                  itemBuilder: (context, index) {
                    final b = bookings[index];
                    return ListTile(
                      title: Text("Booking ID: ${b.bookingId}"),
                      subtitle: Text("Event ID: ${b.eventId} • Booked on: ${b.createdAt}"),
                    );
                  },
                ),
    );
  }
}
