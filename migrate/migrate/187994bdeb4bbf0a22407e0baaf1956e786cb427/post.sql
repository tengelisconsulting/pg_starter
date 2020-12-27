DO $$
DECLARE
  v_notifications  UUID[];
BEGIN
  WITH sched AS (
    SELECT ud_h.setting_value::INTEGER hours,
           ud_m.setting_value::INTEGER minutes,
           'DAY_END'::NOTIFICATION_T notification_type
      FROM user_default ud_h
      JOIN user_default ud_m
        ON ud_m.setting_name = 'DAY_END_SCHED_M'
     WHERE ud_h.setting_name = 'DAY_END_SCHED_H'
  ), users AS (
     SELECT u.user_id
       FROM ac_user u
  LEFT JOIN user_notification un
         ON un.user_id = u.user_id
        AND un.notification_type = 'DAY_END'::NOTIFICATION_T
      WHERE un.notification_id IS NULL
  )
       SELECT array_agg(
                user_notification_create(
                  p_user_id => u.user_id,
                  p_notification_type => s.notification_type,
                  p_sched_time_h => s.hours,
                  p_sched_time_m => s.minutes
                )
              )
         INTO v_notifications
        FROM users u
  CROSS JOIN sched s
  ;
END;
$$ LANGUAGE plpgsql;
