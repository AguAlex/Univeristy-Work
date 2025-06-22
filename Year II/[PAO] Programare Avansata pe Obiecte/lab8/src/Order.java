public class Order {

    private int id;
    private OrderStatus status;

    public void printStatus() {
        System.out.println(status);
    }

    public void setStatusPlaced() {
        status = OrderStatus.PLACED;
    }
    public void setStatusShipped() {
        status = OrderStatus.SHIPPED;
    }
    public void setStatusDelivered() {
        status = OrderStatus.DELIVERED;
    }
    public void setStatusCancelled() {
        status = OrderStatus.CANCELLED;
    }
}
