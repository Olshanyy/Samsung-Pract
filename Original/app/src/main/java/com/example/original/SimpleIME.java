package com.example.original;

import android.annotation.SuppressLint;
import android.inputmethodservice.InputMethodService;
import android.inputmethodservice.Keyboard;
import android.inputmethodservice.KeyboardView;
import android.inputmethodservice.KeyboardView.OnKeyboardActionListener;
import android.os.Build;
//import android.support.annotation.RequiresApi;
import android.view.KeyEvent;
import android.view.MotionEvent;
import android.view.View;
import android.view.inputmethod.InputConnection;

import androidx.annotation.RequiresApi;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;


public abstract class SimpleIME extends InputMethodService
        implements OnKeyboardActionListener{

    private KeyboardView kv;
    private Keyboard keyboard;

    public List<Keyboard.Key> keys;
    public static HashMap<String, ArrayList<String>> keysdata = new HashMap<>();

    public static boolean start_collecting = false;

    private boolean caps = false;


    @Override
    public void onPress(int primaryCode) {}

    @Override
    public void onRelease(int primaryCode) {
    }

    @Override
    public void onText(CharSequence text) {
    }

    @Override
    public void swipeDown() {
    }

    @Override
    public void swipeLeft() {
    }

    @Override
    public void swipeRight() {
    }

    @Override
    public void swipeUp() {
    }

    @SuppressLint("ClickableViewAccessibility")
    @Override
    public View onCreateInputView() {
        kv = (KeyboardView)getLayoutInflater().inflate(R.layout.keyboard, null);
        keyboard = new Keyboard(this, R.xml.qwerty);
        kv.setKeyboard(keyboard);
        kv.setOnKeyboardActionListener(this);

        keys = keyboard.getKeys();

        kv.setOnTouchListener(new View.OnTouchListener() {
            @RequiresApi(api = Build.VERSION_CODES.N)
            @Override
            public boolean onTouch(View v, MotionEvent event) {
                if (event.getAction() == MotionEvent.ACTION_DOWN) {
//                    String ch = findChar(event.getX(), event.getY());
//
//                    ArrayList<String> keydata = new ArrayList<>();
//                    keydata.add(String.valueOf(System.nanoTime()));
//
//                    keysdata.put(ch, keydata);
                    int a;
                } else if (event.getAction() == MotionEvent.ACTION_UP) {
//                    String ch = findChar(event.getX(), event.getY());
//
//                    ArrayList<String> keydata = keysdata.get(ch);
//                    assert keydata != null;
//                    keydata.add(String.valueOf(System.nanoTime()));
//                    keydata.add(String.valueOf(event.getSize()));
//
//                    keysdata.replace(ch, keydata);
                    int a;
                }

                return true;
            }

//            private String findChar(Float x, Float y){
//                for (Keyboard.Key key : keys) {
//                    if (key.x <= x && x <= (key.x + key.width) &&
//                            key.y <= y && y <= (key.y + key.height)) {
//                        return key.toString();
//                    }
//                }
//
//                return "";
//            }
        });

        return kv;
    }

    @Override
    public void onKey(int primaryCode, int[] keyCodes) {
        InputConnection ic = getCurrentInputConnection();
        switch(primaryCode){
            case Keyboard.KEYCODE_DELETE :
                ic.deleteSurroundingText(1, 0);
                break;
            case Keyboard.KEYCODE_SHIFT:
                caps = !caps;
                keyboard.setShifted(caps);
                kv.invalidateAllKeys();
                break;
            case Keyboard.KEYCODE_DONE:
                ic.sendKeyEvent(new KeyEvent(KeyEvent.ACTION_DOWN, KeyEvent.KEYCODE_ENTER));
                break;
            default:
                char code = (char)primaryCode;
                if(Character.isLetter(code) && caps){
                    code = Character.toUpperCase(code);
                }
                ic.commitText(String.valueOf(code),1);
        }
    }

}
