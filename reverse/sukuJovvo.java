import java.util.Scanner;

// 
// JAWABAN DIDEPAN MATA, BARU GW SADARI SETELAH MIKIR 4 JAM !!!!!!!!!!!!!
// 

public class Main
{
    public static void main(final String[] array) {
        final int[] array2 = { 88, 74, 97, 118, 97, 95, 68, 101, 99, 111, 109, 112, 105, 108, 101 };
        final Scanner scanner = new Scanner(System.in);
        System.out.print("[>] Flag: ");
        final String nextLine = scanner.nextLine();
        System.out.println(nextLine.length());
        System.out.println(array2.length);
        if (nextLine.length() != 15) {
            System.out.println("[!] WRONGooo!");
            System.exit(0);
        }
        for (int i = 0; i < array2.length; ++i) {
            nextLine.charAt(i);
            if (nextLine.charAt(i) != array2[i]) {
                System.out.println("[!] WRONGaaaa!");
                System.exit(0);
            }
        }
        System.out.printf("[FLAG] FostiCTF{%s}\n", nextLine);
    }
}