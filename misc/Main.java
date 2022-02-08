public class Main {

    public static void main(String args[]) {
        int n = Integer.parseInt(args[0]);
        int sum = 0;

        for (int i = 1; i < n; i++) {
            sum += i * i;
        }

        System.out.println("Sum squares from 1 to " + n + " = " + sum);
    }
}
