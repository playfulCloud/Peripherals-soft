package org.example;

import com.google.zxing.BarcodeFormat;
import com.google.zxing.EncodeHintType;
import com.google.zxing.MultiFormatWriter;
import com.google.zxing.client.j2se.MatrixToImageWriter;
import com.google.zxing.common.BitMatrix;
import com.google.zxing.qrcode.decoder.ErrorCorrectionLevel;

import java.nio.file.FileSystems;
import java.nio.file.Path;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class BarcodeGenerator {

    public static String calculateCheckDigit(String eanCode) {
        int sum = 0;
        for (int i = 0; i < eanCode.length(); i++) {
            int digit = Integer.parseInt(eanCode.substring(i, i + 1));
            if (i % 2 == 0) {
                sum += digit;
            } else {
                sum += digit * 3;
            }
        }
        int mod = sum % 10;
        return mod == 0 ? "0" : Integer.toString(10 - mod);
    }

    public static void generateEAN13BarcodeImage(String barcodeText) throws Exception {
        String filePath = "EAN13_Barcode.png";
        String charset = "UTF-8";
        Map<EncodeHintType, ErrorCorrectionLevel> hintMap = new HashMap<EncodeHintType, ErrorCorrectionLevel>();
        hintMap.put(EncodeHintType.ERROR_CORRECTION, ErrorCorrectionLevel.L);

        createBarcode(barcodeText, filePath, charset, hintMap, 200, 100);
    }

    public static void createBarcode(String barcodeText, String filePath, String charset,
                                     Map<EncodeHintType, ErrorCorrectionLevel> hintMap,
                                     int width, int height) throws Exception {
        BitMatrix matrix = new MultiFormatWriter().encode(
                new String(barcodeText.getBytes(charset), charset),
                BarcodeFormat.EAN_13,
                width, height,
                hintMap
        );
        Path path = FileSystems.getDefault().getPath(filePath);
        MatrixToImageWriter.writeToPath(matrix, filePath.substring(filePath.lastIndexOf('.') + 1), path);
    }

    public static void main(String[] args) {
        try {
            Scanner keyboard = new Scanner(System.in);
            System.out.println("Enter the 12 digits for your barcode");
            String eanCode = keyboard.nextLine();
            String fullEanCode = eanCode + calculateCheckDigit(eanCode);
            generateEAN13BarcodeImage(fullEanCode);
            System.out.println("Barcode Generated.");
            System.out.println(fullEanCode);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}