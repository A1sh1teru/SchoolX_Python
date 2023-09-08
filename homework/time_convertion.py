def seconds_conversion(seconds):
        h = str(seconds // 3600)
        if len(h)<3:
            h = h + ' час(а/ов)'
        m = str((seconds % 3600) // 60)
        if len(m)<3:
            m = m + ' минут(а/ы)'
        return h + " и " + m

if __name__ == "__main__":
     seconds_arr = [3600, 3601, 3500, 323500]
     for a in seconds_arr:
          print(a, "-->", seconds_conversion(a))