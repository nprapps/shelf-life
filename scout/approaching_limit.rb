require 'date'

class NearingLimit < Scout::Plugin
  def build_report

    log_file_path = '/var/log/cook-your-cupboard.log'
    count = 0

    # Get today's date.
    today = DateTime.now

    # Modify this to be the UTC date.
    # This totally sucks.
    today = today.new_offset(Rational(0, 24))

    # Now, add four hours to that date.
    # This also sucks.
    today = today - Rational(60 * 60 * 4, 86400)

    File.open(log_file_path) do |file|
      file.each do |line|

        file_date = line.split(' ')[0]
        file_time = line.split(' ')[1]

        this_date = DateTime.parse(file_date)

        if this_date == today
          if line.split(' ')[2] == 'INFO'
            count += 1
          end
        end

      end
    end

    report(:successful_posts => count)

  end
end

