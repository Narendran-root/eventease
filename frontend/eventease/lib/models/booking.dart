class Booking {
  final String bookingId;
  final int eventId;
  final int userId;
  final String createdAt;

  Booking({
    required this.bookingId,
    required this.eventId,
    required this.userId,
    required this.createdAt,
  });

  factory Booking.fromJson(Map<String, dynamic> json) {
    return Booking(
      bookingId: json['booking_id'],
      eventId: json['event_id'],
      userId: json['user_id'],
      createdAt: json['created_at'],
    );
  }
}
