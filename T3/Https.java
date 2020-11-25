// java Https message key
// java Https 8A1DE7DD177FAE564A696092F36D672CA705ABFB171B940E9118D357FE4C31E2CB657F889745AA4A038B08477EFBA6A005C9FB45E2967E8DAC7FE34FFDC6B16388FF6F4033E99607F335814937433086C188CCC43652408636988743EC6EE7BD12B8E1A3C7EF1861EDE28D9F9EAC668E FAE9223FEB4CA59080BFB1378FEA56F0
// java Https C90FEC1B98343532335AC48153F164FC5EEBFEDDE1BFF9132B0C18678B454373029C27973042F7BB71B97FB5B5B9EE8B218386A40C5267B567C753E9468D698CF8281CB0ECCFF9548DED280D426EB78DCC33CCAB8AE88C5989EC6C3ACD538375 FAE9223FEB4CA59080BFB1378FEA56F0
import java.util.Scanner;
import javax.crypto.*;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.PBEKeySpec;
import javax.crypto.spec.SecretKeySpec;
import java.math.BigInteger;

public class Https {
    public static BigInteger p;
    public static BigInteger g;

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

    public static String stringToHexString(String str){
 
	  char[] chars = str.toCharArray();
 
	  StringBuffer hex = new StringBuffer();
	  for(int i = 0; i < chars.length; i++){
	    hex.append(Integer.toHexString((int)chars[i]));
	  }
 
	  return hex.toString();
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

    public static byte[] encrypt(byte[] msg, byte[] key) {
        byte[] ciphered = new byte[5];
        try {
            Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
            SecretKeySpec secretKey = new SecretKeySpec(key, "AES");
            byte[] iv = cipher.getParameters().getParameterSpec(IvParameterSpec.class).getIV();
        
            cipher.init(Cipher.ENCRYPT_MODE, secretKey, new IvParameterSpec(iv));
            ciphered = cipher.doFinal(msg);

        } catch(Exception error) {
            System.out.println(error);
        }
        return ciphered;
    }

    public static void A(){
        int a = 1434365;
        BigInteger A = g.pow(a);
        A = A.remainder(p);
        System.out.println("A"+ A);
        System.out.println(byteArrayToHexString(A.toByteArray()));  
    }

    public static void main(String[] args) {
        String hexP = "0B10B8F96A080E01DDE92DE5EAE5D54EC52C99FBCFB06A3C69A6A9DCA52D23B616073E28675A23D189838EF1E2EE652C013ECB4AEA906112324975C3CD49B83BFACCBDD7D90C4BD7098488E9C219A73724EFFD6FAE5644738FAA31A4FF55BCCC0A151AF5F0DC8B4BD45BF37DF365C1A65E68CFDA76D4DA708DF1FB2BC2E4A4371";
        String hexG = "0A4D1CBD5C3FD34126765A442EFB99905F8104DD258AC507FD6406CFF14266D31266FEA1E5C41564B777E690F5504F213160217B4B01B886A5E91547F9E2749F4D7FBD7D3B9A92EE1909D0D2263F80A76A6A24C087A091F531DBF0A0169B6A28AD662A4D18E73AFA32D779D5918D08BC8858F4DCEF97C2A24855E6EEB22B3B2E5";
        p = new BigInteger(hexP, 16);
        g = new BigInteger(hexG, 16);
        // A();
        // -----------------------------
        String message = args[0];
        byte[] key = hexStringToByteArray(args[1]);        
        byte[] iv = hexStringToByteArray( message.substring(0, 32) );
        byte[] msg = hexStringToByteArray( message.substring(32) );

        byte[] decryptedBytes = decrypt(msg, key, iv);
        String decryptedString = hexStringToString(byteArrayToHexString(decryptedBytes));
        System.out.println("\n" + decryptedString); 

        StringBuilder sb = new StringBuilder(decryptedString);  
        msg = hexStringToByteArray(stringToHexString(sb.reverse().toString())); // reverserd string in bytes

        String encryptedHex = byteArrayToHexString(encrypt(msg, key));
        System.out.println("\n" + encryptedHex);

    }
}
//8A1DE7DD177FAE564A696092F36D672CA705ABFB171B940E9118D357FE4C31E2CB657F889745AA4A038B08477EFBA6A005C9FB45E2967E8DAC7FE34FFDC6B16388FF6F4033E99607F335814937433086C188CCC43652408636988743EC6EE7BD12B8E1A3C7EF1861EDE28D9F9EAC668E FAE9223FEB4CA59080BFB1378FEA56F0
//0E748C17A0D01891B104D606A9D6DD663207D99600D2C0F12A2226779547E23794C0A3EEADC8D3CBBB3FB2F5F55FD7B743EB0C6B522219012B1D360D3AB1DFE7FB823FEB9FFC27B6E3577208C5A72A015EBB01B15AEA48B61B4F7A49A06B4BEC