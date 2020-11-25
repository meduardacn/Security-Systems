// java Https message key
// java Https E1DD68F3DF6E014DD50FCAE334CB63D1F0CA66608F48E38E9A40E31E9D266C985B708A5C106F3CC208083F547B19D9B2C5A9E4F5DAF2F5208FE3A1D3F01143D3A94DF90EA450C414FB1D127D9E1447A726B58E86CD7E81A089F59AC089A4771BD360EA54E14DC81E12A677DAB1A700CB AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
import java.util.Scanner;
import javax.crypto.*;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.PBEKeySpec;
import javax.crypto.spec.SecretKeySpec;

public class Https {
    public  static byte[] hexStringToByteArray(String s){
        int len = s.length();
        byte[] data = new byte[len / 2];
        for (int i = 0; i < len; i += 2){
            data[i / 2] = (byte) ((Character.digit(s.charAt(i), 16) << 4) + Character.digit(s.charAt(i+1), 16));
        }
        return data;
    }

    public static void main(String[] args) {
        String message = args[0];
        String key = args[1];

        byte[] password = hexStringToByteArray(key);
        
        String IV = message.substring(0, 32);
        String msg = message.substring(32);

        System.out.println("Message:\n" + message + "\n");

        System.out.println(password);    
        System.out.println(IV + " " + msg);
    }
}