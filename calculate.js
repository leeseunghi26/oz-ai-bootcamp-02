import java.util.Scanner;

public class ConsoleCalculator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("=== 자바 콘솔 계산기 ===");
        
        // 1. 첫 번째 숫자 입력
        System.out.print("첫 번째 숫자를 입력하세요: ");
        double num1 = sc.nextDouble();

        // 2. 연산자 입력
        System.out.print("연산자를 입력하세요 (+, -, *, /): ");
        char operator = sc.next().charAt(0);

        // 3. 두 번째 숫자 입력
        System.out.print("두 번째 숫자를 입력하세요: ");
        double num2 = sc.nextDouble();

        double result = 0;
        boolean success = true;

        // 4. 연산 로직 (조건문 활용)
        switch (operator) {
            case '+': result = num1 + num2; break;
            case '-': result = num1 - num2; break;
            case '*': result = num1 * num2; break;
            case '/':
                if (num2 != 0) {
                    result = num1 / num2;
                } else {
                    System.out.println("오류: 0으로 나눌 수 없습니다.");
                    success = false;
                }
                break;
            default:
                System.out.println("오류: 잘못된 연산자입니다.");
                success = false;
        }

        // 5. 결과 출력
        if (success) {
            System.out.println("결과: " + num1 + " " + operator + " " + num2 + " = " + result);
        }
        
        sc.close();
    }
}