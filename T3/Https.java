// java Https message key
// java Https E1DD68F3DF6E014DD50FCAE334CB63D1F0CA66608F48E38E9A40E31E9D266C985B708A5C106F3CC208083F547B19D9B2C5A9E4F5DAF2F5208FE3A1D3F01143D3A94DF90EA450C414FB1D127D9E1447A726B58E86CD7E81A089F59AC089A4771BD360EA54E14DC81E12A677DAB1A700CB AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
import java.util.Scanner;
import javax.crypto.*;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.PBEKeySpec;
import javax.crypto.spec.SecretKeySpec;
import java.math.BigInteger;

public class Https {

    public  static byte[] hexStringToByteArray(String s) {
        int len = s.length();
        byte[] data = new byte[len / 2];
        for (int i = 0; i < len; i += 2){
            data[i / 2] = (byte) ((Character.digit(s.charAt(i), 16) << 4) + Character.digit(s.charAt(i+1), 16));
        }
        return data;
    }

    public static String hexStringToString(String hex) {
 
        StringBuilder sb = new StringBuilder();
        StringBuilder temp = new StringBuilder();
    
        for( int i=0; i<hex.length()-1; i+=2 ){
    
            String output = hex.substring(i, (i + 2));
            int decimal = Integer.parseInt(output, 16);
            sb.append((char)decimal);
            temp.append(decimal);
        }
    
        return sb.toString();
    }

    public static String byteArrayToHexString(byte[] b){
        StringBuffer sb = new StringBuffer(b.length * 2);
        for (int i = 0; i < b.length; i++) {
            int v = b[i] & 0xff;
            if (v < 16) {
                sb.append('0');
            }
            sb.append(Integer.toHexString(v));
        }
        return sb.toString().toUpperCase();
    }
    public static byte[] decrypt(byte[] msg, byte[] key, byte[] iv){
        byte[] deciphered = new byte[5];
        try {
            Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
            SecretKeySpec secretKey = new SecretKeySpec(key, "AES");

            cipher.init(Cipher.DECRYPT_MODE, secretKey, new IvParameterSpec(iv));
            deciphered = cipher.doFinal(msg);
        
        } catch(Exception error) {
            System.out.println(error);
        }
        return deciphered;
    }

    public static void main(String[] args) {
        String message = args[0];
        byte[] key = hexStringToByteArray(args[1]);        
        byte[] iv = hexStringToByteArray( message.substring(0, 32) );
        byte[] msg = hexStringToByteArray( message.substring(32) );


        byte[] decryptedBytes = decrypt(msg, key, iv);
        String decryptedString = hexStringToString(byteArrayToHexString(decryptedBytes));
        
        System.out.println(key);    
        System.out.println(iv + " " + msg);

        System.out.println("\n" + decryptedString); 

    }
}